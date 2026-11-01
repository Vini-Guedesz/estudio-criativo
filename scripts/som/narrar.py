"""narrar.py — narração com voz pronta, local e grátis (Kokoro, vozes em português do Brasil).

O roteiro tem uma frase por linha (padrão da skill canal-dark). Cada linha vira um trecho de voz com uma pausa
curta depois; uma linha em branco vira uma pausa longa (troca de parte). Linhas que começam com # são ignoradas
(títulos e anotações do roteiro).
Saída: WAV 24 kHz mono, voz seca (o volume final é acertado na mixagem, regras.md). Ao fim, mostra a duração e
as palavras por minuto, o número que vai para as normas do canal.

Precisa do extra de voz: uv sync --extra gpu --extra voz (ou --extra cpu --extra voz sem placa NVIDIA).

Uso:
  uv run scripts/som/narrar.py roteiro.md --voz pf_dora --saida audio/narracao.wav
  uv run scripts/som/narrar.py --texto "Uma frase só." --voz pm_alex --saida teste.wav
  uv run scripts/som/narrar.py roteiro.md --voz pm_alex --velocidade 0.95 --saida audio/narracao.wav
  uv run scripts/som/narrar.py amostras --saida pasta/      # o mesmo texto em todas as vozes pt-BR, para escolher
  uv run scripts/som/narrar.py vozes                         # lista as vozes
Mistura de vozes: --voz "pm_alex,pm_santa" (média das duas).
"""
from __future__ import annotations

import argparse, re, sys, warnings
from pathlib import Path

import numpy as np
import soundfile as sf

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
warnings.filterwarnings("ignore")

SR = 24000
VOZES = {
    "pf_dora": "feminina",
    "pm_alex": "masculina",
    "pm_santa": "masculina",
}
PAUSA_FRASE, PAUSA_PARTE = 0.35, 0.8
TEXTO_AMOSTRA = """Você já reparou que seu corpo arrepia quando ouve uma música bonita?
Parece só um detalhe... mas esse arrepio tem pelo menos seis milhões de anos.

Em dois mil e onze, pesquisadores da Universidade McGill mediram o cérebro de pessoas ouvindo suas músicas favoritas.
O resultado surpreendeu: o arrepio vinha junto com uma descarga de dopamina!
Então por que o corpo faria isso com uma simples melodia?
A resposta está num mecanismo muito mais antigo do que a música."""


def linhas_do_roteiro(texto: str) -> list[str | None]:
    """Uma entrada por frase; None marca a pausa longa de uma linha em branco."""
    saida: list[str | None] = []
    for linha in texto.splitlines():
        linha = linha.strip()
        if not linha:
            if saida and saida[-1] is not None:
                saida.append(None)
            continue
        if linha.startswith("#") or linha.startswith(">"):
            continue
        linha = re.sub(r"[*_`]", "", linha)  # marcação de markdown não é lida
        saida.append(linha)
    while saida and saida[-1] is None:
        saida.pop()
    return saida


def pipeline():
    try:
        from kokoro import KPipeline
    except ImportError:
        sys.exit("Kokoro não instalado. Rode: uv sync --extra gpu --extra voz")
    import torch
    dispositivo = "cuda" if torch.cuda.is_available() else "cpu"
    return KPipeline(lang_code="p", repo_id="hexgrad/Kokoro-82M", device=dispositivo), dispositivo


def sintetizar(kp, frases: list[str | None], voz: str, velocidade: float) -> np.ndarray:
    pedacos: list[np.ndarray] = []
    for frase in frases:
        if frase is None:
            pedacos.append(np.zeros(int(SR * (PAUSA_PARTE - PAUSA_FRASE)), dtype=np.float32))
            continue
        for _, _, audio in kp(frase, voice=voz, speed=velocidade):
            if audio is not None:
                pedacos.append(np.asarray(audio, dtype=np.float32))
        pedacos.append(np.zeros(int(SR * PAUSA_FRASE), dtype=np.float32))
    if not pedacos:
        sys.exit("Nada para narrar: o texto está vazio.")
    return np.concatenate(pedacos)


def relatorio(audio: np.ndarray, frases: list[str | None], destino: Path) -> str:
    seg = len(audio) / SR
    palavras = sum(len(f.split()) for f in frases if f)
    ppm = palavras / (seg / 60) if seg else 0
    return f"{destino}  ·  {seg:.1f} s  ·  {palavras} palavras  ·  {ppm:.0f} palavras/min"


def checar_voz(voz: str):
    for v in voz.split(","):
        if v not in VOZES:
            sys.exit(f"Voz desconhecida: {v}. Vozes pt-BR: {', '.join(VOZES)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("roteiro", nargs="?", help="arquivo do roteiro (.md/.txt), 'amostras' ou 'vozes'")
    ap.add_argument("--texto", help="texto direto, no lugar de um arquivo")
    ap.add_argument("--voz", default="pf_dora", help="pf_dora, pm_alex, pm_santa ou mistura 'a,b'")
    ap.add_argument("--velocidade", type=float, default=1.0, help="1.0 = normal; 0.9 mais lento")
    ap.add_argument("--saida", help="arquivo .wav (ou pasta, em 'amostras')")
    a = ap.parse_args()

    if a.roteiro == "vozes":
        for v, tipo in VOZES.items():
            print(f"{v:10} {tipo}")
        return

    if a.roteiro == "amostras":
        pasta = Path(a.saida or "amostras-de-voz")
        pasta.mkdir(parents=True, exist_ok=True)
        frases = linhas_do_roteiro(a.texto or TEXTO_AMOSTRA)
        kp, disp = pipeline()
        print(f"Gerando amostras ({disp})...")
        for voz in VOZES:
            audio = sintetizar(kp, frases, voz, a.velocidade)
            destino = pasta / f"amostra-{voz}.wav"
            sf.write(destino, audio, SR)
            print(relatorio(audio, frases, destino))
        return

    if a.texto:
        texto = a.texto
    elif a.roteiro:
        texto = Path(a.roteiro).read_text(encoding="utf-8")
    else:
        ap.error("passe um roteiro, --texto, 'amostras' ou 'vozes'")
    if not a.saida:
        ap.error("--saida é obrigatório (ex.: audio/narracao.wav)")
    checar_voz(a.voz)
    frases = linhas_do_roteiro(texto)
    kp, disp = pipeline()
    audio = sintetizar(kp, frases, a.voz, a.velocidade)
    destino = Path(a.saida)
    destino.parent.mkdir(parents=True, exist_ok=True)
    sf.write(destino, audio, SR)
    print(relatorio(audio, frases, destino))


if __name__ == "__main__":
    main()
