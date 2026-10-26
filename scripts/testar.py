"""Teste automático dos scripts do estúdio: cria uma marca temporária, exercita tudo e apaga no fim.

Uso (da raiz do estúdio):
    uv run scripts/testar.py

Confere: regras de nome (Python e Node iguais), criação de marca e peças, rascunhos e versões, aprovação para
final/, gerador de post (se as bibliotecas de design estiverem instaladas), tokens, mural e renomear.
Não toca nas marcas de verdade: tudo acontece em 04-marcas/teste-automatico-zz/, que é apagada mesmo se algo falhar.
Rode depois de mexer em qualquer script de scripts/ ou scripts/design/. Sai com erro se algum item falhar.
"""
from __future__ import annotations

import shutil
import subprocess
import sys
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _estudio import MARCAS, RAIZ, nome_final, rascunho, slug  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

NOME, NOME_2 = "Teste Automático Zz", "Teste Automático Yy"
PASTA, PASTA_2 = MARCAS / slug(NOME), MARCAS / slug(NOME_2)
DESIGN = RAIZ / "scripts" / "design"
NODE = shutil.which("node")
resultados: list[tuple[str, bool, str]] = []


def confere(nome: str, ok: bool, detalhe: str = ""):
    resultados.append((nome, bool(ok), detalhe))
    print(f"  {'ok ' if ok else 'FALHOU'}  {nome}" + (f"  ({detalhe})" if detalhe and not ok else ""))


def py(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, *args], cwd=RAIZ, capture_output=True, text=True, encoding="utf-8", errors="replace")


def node(script: str, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run([NODE, str(DESIGN / script), *args], cwd=DESIGN, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", env={**__import__("os").environ, "INIT_CWD": str(RAIZ)})


def tamanho_png(arq: Path) -> tuple[int, int]:
    b = arq.read_bytes()[16:24]
    return int.from_bytes(b[:4], "big"), int.from_bytes(b[4:], "big")


def testes():
    print("\nRegras de nome")
    p = MARCAS / "m" / "reels" / "2026-01-01-lancamento"
    casos = {"lancamento-reels-v3.mp4": "lancamento-reels.mp4", "lancamento-reels-v3-som.mp4": "lancamento-reels.mp4",
             "lancamento-reels-legenda-v2.txt": "lancamento-reels-legenda.txt", "lancamento-reels-capa-v1.png": "lancamento-reels-capa.png"}
    for entrada, esperado in casos.items():
        confere(f"final de {entrada}", nome_final(p / "rascunhos" / entrada).name == esperado)
    c = MARCAS / "m" / "carrosseis" / "2026-01-01-5-erros"
    confere("final de tela de carrossel", nome_final(c / "rascunhos" / "5-erros-carrossel-v2-01.png").name == "5-erros-carrossel-01.png")
    amostras = ["Lançamento da Coleção!", "Café do Zé", "  São Luís – Sem Fila  "]
    confere("slug em Python", slug(amostras[0]) == "lancamento-da-colecao")
    if NODE:
        js = subprocess.run([NODE, "-e", "import('./estudio.mjs').then(m=>console.log(JSON.stringify(process.argv.slice(1).map(m.slug))))", *amostras],
                            cwd=DESIGN, capture_output=True, text=True, encoding="utf-8")
        confere("slug igual em Python e Node", js.stdout.strip() == str([slug(a) for a in amostras]).replace("'", '"').replace(", ", ","), js.stdout.strip() or js.stderr[-200:])

    print("\nMarca e peças")
    r = py("scripts/peca.py", "marca", NOME)
    confere("cria a marca", r.returncode == 0 and PASTA.exists(), r.stderr[-200:])
    confere("ficha com o nome", (PASTA / "README.md").read_text(encoding="utf-8").startswith(f"# {NOME}"))
    datas = [f.name for f in PASTA.rglob("*.md") if f.name != "briefing.md" and "AAAA-MM-DD" in f.read_text(encoding="utf-8")]
    confere("datas preenchidas (mural, calendário, resultados)", not datas, ", ".join(datas))
    for t in ("reels", "posts", "carrosseis"):
        r = py("scripts/peca.py", "nova", t, "Peça de teste", "--marca", PASTA.name, "--data", "2026-01-01")
        confere(f"cria peça em {t}", r.returncode == 0, r.stderr[-200:])
    reels = PASTA / "reels" / "2026-01-01-peca-de-teste"
    post = PASTA / "posts" / "2026-01-01-peca-de-teste"
    carr = PASTA / "carrosseis" / "2026-01-01-peca-de-teste"
    confere("vídeo tem audio/, motor/, revisao/ e roteiro.md", all((reels / x).exists() for x in ("audio", "motor", "revisao", "roteiro.md")))
    confere("post não tem audio/ nem motor/", not (post / "audio").exists() and not (post / "motor").exists())
    confere("toda peça tem copy.md, rascunhos/ e final/", all((x / f).exists() for x in (reels, post, carr) for f in ("copy.md", "rascunhos", "final")))

    print("\nRascunhos e aprovação")
    confere("primeiro rascunho é v1", rascunho(reels, "mp4").name == "peca-de-teste-reels-v1.mp4")
    (reels / "rascunhos" / "peca-de-teste-reels-v1.mp4").write_bytes(b"x")
    confere("depois do v1 vem o v2", rascunho(reels, "mp4").name == "peca-de-teste-reels-v2.mp4")
    confere("extra tem versão própria", rascunho(reels, "txt", extra="legenda").name == "peca-de-teste-reels-legenda-v1.txt")
    confere("tela de carrossel", rascunho(carr, "png", parte=3).name == "peca-de-teste-carrossel-v1-03.png")
    r = py("scripts/peca.py", "aprovar", str(reels / "rascunhos" / "peca-de-teste-reels-v1.mp4"))
    confere("aprovar copia para final/ com nome limpo", (reels / "final" / "peca-de-teste-reels.mp4").exists(), r.stderr[-200:])
    confere("aprovar anota em Entregas", "final/peca-de-teste-reels.mp4" in (reels / "README.md").read_text(encoding="utf-8"))

    print("\nDesign (Node)")
    if not NODE or not (DESIGN / "node_modules" / "satori").exists():
        print("  --   pulado: bibliotecas de design não instaladas (npm install em scripts/design)")
    else:
        r = node("tokens.mjs", "--marca", PASTA.name)
        confere("tokens geram o CSS", (PASTA / "identidade" / "design-tokens" / "saida" / "marca.css").exists(), r.stderr[-200:])
        r1 = node("post.mjs", "--peca", str(carr), "--parte", "1", "Título de teste", "Apoio de teste")
        r2 = node("post.mjs", "--peca", str(carr), "--parte", "2", "--mesma-versao", "--layout", "conteudo", "--numero", "2", "Outro título")
        r3 = node("post.mjs", "--peca", str(carr), "--parte", "3", "--mesma-versao", "--layout", "cta", "Chamada")
        nomes = sorted(f.name for f in (carr / "rascunhos").glob("*.png"))
        esperado = [f"peca-de-teste-carrossel-v1-0{i}.png" for i in (1, 2, 3)]
        confere("post gera as 3 telas com o nome do padrão", nomes == esperado, (r1.stderr or r2.stderr or r3.stderr)[-200:] or str(nomes))
        if nomes:
            confere("post tem 1080x1350", tamanho_png(carr / "rascunhos" / nomes[0]) == (1080, 1350))
        for e in ("neobrutalismo", "minimalismo-suico", "luxo-escuro"):
            r = node("post.mjs", "--peca", str(post), "--estilo", e, "Título")
            confere(f"post no estilo {e}", r.returncode == 0, r.stderr[-200:])
        r = node("post.mjs", "--peca", str(post), "--estilo", "inexistente", "Título")
        confere("estilo inexistente dá erro claro", r.returncode != 0 and "não tem modelo" in r.stderr)

    print("\nMural")
    mural = PASTA / "referencias" / "mural.md"
    texto = mural.read_text(encoding="utf-8")
    texto = texto.replace("## Reels e vídeos curtos\n\n| Link | O que chamou atenção | Estilo | Status |\n|---|---|---|---|\n",
                          "## Reels e vídeos curtos\n\n| Link | O que chamou atenção | Estilo | Status |\n|---|---|---|---|\n"
                          "| https://exemplo.invalid/a | teste | | novo |\n| https://exemplo.invalid/b | teste | | analisado · analises/x.md |\n")
    texto = texto.replace("## Perfis para acompanhar\n\n| Link | O que chamou atenção | Estilo | Status |\n|---|---|---|---|\n",
                          "## Perfis para acompanhar\n\n| Link | O que chamou atenção | Estilo | Status |\n|---|---|---|---|\n| https://exemplo.invalid/c | perfil | | |\n")
    mural.write_text(texto, encoding="utf-8")
    r = py("scripts/referencias.py", "mural", "--marca", PASTA.name)
    confere("mural conta os status", "1 analisado, 2 novo" in r.stdout, r.stdout[:200] + r.stderr[-200:])
    confere("dica do mural traz a marca", f"--marca {PASTA.name} --baixar" in r.stdout)

    print("\nRenomear")
    r = py("scripts/peca.py", "renomear", NOME_2, "--marca", PASTA.name)
    confere("renomeia a pasta", PASTA_2.exists() and not PASTA.exists(), r.stderr[-200:])
    confere("troca o título da ficha", (PASTA_2 / "README.md").read_text(encoding="utf-8").startswith(f"# {NOME_2}"))
    r = py("scripts/peca.py", "renomear", NOME, "--marca", PASTA_2.name)
    confere("volta ao nome original", PASTA.exists() and not PASTA_2.exists(), r.stderr[-200:])


def main():
    if PASTA.exists() or PASTA_2.exists():
        sys.exit(f"erro: já existe {PASTA.name} ou {PASTA_2.name} em 04-marcas/ (sobra de um teste anterior?). Apague e rode de novo.")
    print("Teste automático do estúdio (marca temporária em 04-marcas/" + PASTA.name + ")")
    try:
        testes()
    except Exception:  # noqa: BLE001
        confere("o teste rodou até o fim", False, traceback.format_exc(limit=3)[-400:])
    finally:
        for pasta in (PASTA, PASTA_2):
            shutil.rmtree(pasta, ignore_errors=True)
    falhas = [n for n, ok, _ in resultados if not ok]
    print(f"\n{len(resultados) - len(falhas)} de {len(resultados)} ok. Marca temporária apagada.")
    if falhas:
        print("Falharam: " + "; ".join(falhas))
        sys.exit(1)


if __name__ == "__main__":
    main()
