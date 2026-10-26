"""Renderiza um HTML em PNG nos tamanhos do estúdio (provas de direção, telas, capas), esperando as fontes carregarem.

Uso (da raiz do estúdio):
  uv run scripts/design/render.py <arquivo.html> --saida <imagem.png> [--tamanho post|reels|quadrado|youtube|LxA]

Tamanhos: post 1080x1350 · reels 1080x1920 · quadrado 1080x1080 · youtube 1280x720, ou qualquer LxA (ex.: 1600x1000).
O HTML pode carregar fontes do Google Fonts (precisa de internet) ou das cores e fontes da marca em
04-marcas/<marca>/identidade/design-tokens/saida/marca.css (caminho relativo ao HTML).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

TAMANHOS = {"post": (1080, 1350), "reels": (1080, 1920), "quadrado": (1080, 1080), "youtube": (1280, 720)}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("html")
    ap.add_argument("--saida", required=True)
    ap.add_argument("--tamanho", default="post")
    a = ap.parse_args()
    if a.tamanho in TAMANHOS:
        largura, altura = TAMANHOS[a.tamanho]
    else:
        try:
            largura, altura = (int(x) for x in a.tamanho.lower().split("x"))
        except ValueError:
            sys.exit(f"erro: tamanho '{a.tamanho}' inválido. Use {', '.join(TAMANHOS)} ou LxA")
    html = Path(a.html).resolve()
    if not html.exists():
        sys.exit(f"erro: não achei {a.html}")
    saida = Path(a.saida)
    saida.parent.mkdir(parents=True, exist_ok=True)

    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        nav = p.chromium.launch()
        pag = nav.new_page(viewport={"width": largura, "height": altura})
        pag.goto(html.as_uri(), wait_until="networkidle")
        pag.evaluate("document.fonts.ready")
        pag.wait_for_timeout(300)
        pag.screenshot(path=str(saida))
        nav.close()
    print(f"imagem salva em {saida} ({largura}x{altura})")


if __name__ == "__main__":
    main()
