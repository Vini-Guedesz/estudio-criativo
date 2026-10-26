"""Extrai a paleta de cores de uma referência (print, foto, logo) e mostra o contraste com branco e preto.
Uso: uv run scripts/design/paleta.py caminho/da/imagem.jpg [quantidade]"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from colorthief import ColorThief
from coloraide import Color

qtd = int(sys.argv[2]) if len(sys.argv) > 2 else 6
for r, g, b in ColorThief(sys.argv[1]).get_palette(color_count=qtd, quality=1):
    c = Color("srgb", [r / 255, g / 255, b / 255])
    print(f"{c.to_string(hex=True)}   contraste c/ branco {c.contrast('white'):4.1f}   c/ preto {c.contrast('black'):4.1f}")
print("Dica: texto precisa de contraste 4.5 ou mais para ser legível.")
