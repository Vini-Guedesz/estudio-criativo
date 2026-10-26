"""Caminhos do estúdio, para todo script achar as pastas sem caminho fixo.

Uso nos scripts:
    import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
    from _estudio import RAIZ, BIBLIOTECA, SFX, MUSICA, REFERENCIAS, midia_referencias
    from _estudio import MARCAS, marca, peca, rascunho, nome_final   # marcas e peças (vídeos, posts...)

O padrão das pastas das marcas está em 04-marcas/_LEIA.md; o scripts/design/estudio.mjs repete
as mesmas regras para os scripts Node. Mudou aqui? Mude lá também.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
BIBLIOTECA = RAIZ / "05-biblioteca"
SOM = BIBLIOTECA / "som"
SFX = Path(os.environ.get("ESTUDIO_SFX", SOM / "sfx"))
MUSICA = Path(os.environ.get("ESTUDIO_MUSICA", BIBLIOTECA / "musica"))
FONTES = BIBLIOTECA / "fontes"
REFERENCIAS = RAIZ / "03-referencias"
MARCAS = RAIZ / "04-marcas"

# Tipo de peça → (sufixo do arquivo, é vídeo?). Cada tipo é uma pasta dentro da marca.
TIPOS = {
    "reels": ("reels", True),
    "videos": ("video", True),
    "stories": ("story", True),
    "posts": ("post", False),
    "carrosseis": ("carrossel", False),
}
APELIDOS = {"reel": "reels", "video": "videos", "story": "stories", "post": "posts",
            "carrossel": "carrosseis", "carousel": "carrosseis"}
PASTAS_PECA = ["referencias", "assets", "rascunhos", "final"]
PASTAS_VIDEO = ["audio", "motor", "revisao"]


def midia_referencias() -> Path:
    """Pasta onde fica a mídia das referências: lê o '- **Caminho da mídia:**' do ONDE.md."""
    onde = REFERENCIAS / "ONDE.md"
    if onde.exists():
        m = re.search(r"\*\*Caminho da mídia:\*\*\s*(.+)", onde.read_text(encoding="utf-8"))
        if m:
            caminho = Path(m.group(1).strip().strip("`"))
            return caminho if caminho.is_absolute() else RAIZ / caminho
    return REFERENCIAS


# Marcas e peças -----------------------------------------------------------------

def slug(texto: str) -> str:
    """'Lançamento da Coleção!' → 'lancamento-da-colecao'."""
    import unicodedata
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def tipo(nome: str) -> str:
    """Nome do tipo (aceita singular: 'post', 'reel'...) → pasta do tipo ('posts', 'reels'...)."""
    t = APELIDOS.get(slug(nome), slug(nome))
    if t not in TIPOS:
        raise SystemExit(f"erro: tipo '{nome}' não existe. Use: {', '.join(TIPOS)}")
    return t


def marcas() -> list[Path]:
    """Pastas das marcas criadas (os modelos começam com '_' e ficam de fora)."""
    return sorted(p for p in MARCAS.iterdir() if p.is_dir() and not p.name.startswith(("_", "."))) if MARCAS.exists() else []


def marca(nome: str | None = None) -> Path:
    """Pasta da marca. Sem nome, usa a única marca que existir."""
    if nome:
        p = MARCAS / slug(nome)
        if not p.exists():
            raise SystemExit(f"erro: a marca '{nome}' não existe em 04-marcas/. Crie com: uv run scripts/peca.py marca \"{nome}\"")
        return p
    todas = marcas()
    if len(todas) == 1:
        return todas[0]
    if not todas:
        raise SystemExit("erro: ainda não há marca. Crie com: uv run scripts/peca.py marca \"Nome da marca\"")
    raise SystemExit(f"erro: há mais de uma marca; diga qual com --marca ({', '.join(p.name for p in todas)})")


def peca(caminho: str | Path) -> Path:
    """Acha a pasta de uma peça pelo caminho ou só pelo nome da pasta (ex.: '2026-10-25-lancamento')."""
    p = Path(caminho)
    for c in (p, RAIZ / p):
        if c.is_dir():
            return c.resolve()
    achadas = [d for d in MARCAS.glob(f"*/*/{p.name}") if d.is_dir() and not d.parts[-3].startswith("_")]
    if len(achadas) == 1:
        return achadas[0]
    raise SystemExit(f"erro: não achei a peça '{caminho}'" + (f" (há {len(achadas)} com esse nome)" if achadas else ""))


def _partes_peca(pasta: Path) -> tuple[str, str]:
    """(tema, sufixo) de uma peça: 04-marcas/<marca>/reels/2026-10-25-lancamento → ('lancamento', 'reels')."""
    tema = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", pasta.name)
    return tema, TIPOS.get(pasta.parent.name, (slug(pasta.parent.name), False))[0]


def rascunho(pasta: Path, ext: str, parte: int | None = None, mesma_versao: bool = False,
             extra: str | None = None) -> Path:
    """Próximo arquivo de rascunho: rascunhos/<tema>-<tipo>[-<extra>]-v<N>[-<parte>].<ext>.
    extra = peça complementar com versão própria: 'legenda', 'capa', 'miniatura'..."""
    tema, suf = _partes_peca(pasta)
    if extra:
        suf = f"{suf}-{slug(extra)}"
    ext = ext.lstrip(".")
    versoes = [int(m.group(1)) for f in (pasta / "rascunhos").glob(f"{tema}-{suf}-v*")
               if (m := re.match(rf"{re.escape(tema)}-{re.escape(suf)}-v(\d+)", f.name))]
    n = max(versoes, default=0)
    n = max(n, 1) if mesma_versao else n + 1
    fim = f"-{parte:02d}" if parte else ""
    return pasta / "rascunhos" / f"{tema}-{suf}-v{n}{fim}.{ext}"


def nome_final(arquivo: Path) -> Path:
    """rascunhos/lancamento-reels-v3.mp4 → final/lancamento-reels.mp4.
    A tela do carrossel fica (-01), o extra fica (lancamento-reels-legenda-v2.txt → lancamento-reels-legenda.txt)
    e o '-som' do som.py sai (lancamento-reels-v3-som.mp4 → lancamento-reels.mp4)."""
    pasta = arquivo.resolve().parent.parent
    tema, suf = _partes_peca(pasta)
    nome = arquivo.name
    prefixo = f"{tema}-{suf}"
    if nome.startswith(prefixo):
        nome = prefixo + re.sub(r"-v\d+(?=[-.])", "", nome[len(prefixo):], count=1)
    nome = re.sub(r"-som(?=\.[^.]+$)", "", nome)
    return pasta / "final" / nome


def fonte_da_marca(pasta_marca: Path, papel: str = "titulo", peso: int = 800) -> Path:
    """Arquivo .woff da fonte da marca (fonte.<papel> do marca.json), instalado como @fontsource em scripts/design."""
    import json
    tokens = json.loads((pasta_marca / "identidade" / "design-tokens" / "marca.json").read_text(encoding="utf-8"))
    familia = tokens.get("fonte", {}).get(papel, {}).get("value", "Inter")
    s = slug(familia)
    arq = RAIZ / "scripts" / "design" / "node_modules" / "@fontsource" / s / "files" / f"{s}-latin-{peso}-normal.woff"
    if not arq.exists():
        raise SystemExit(f"erro: a fonte \"{familia}\" (peso {peso}) não está instalada. "
                         f"Instale: npm install @fontsource/{s} --prefix scripts/design")
    return arq
