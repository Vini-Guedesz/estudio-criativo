"""Transforma um logo/desenho em PNG ou JPG em vetor SVG (escala sem perder qualidade).
Uso: uv run scripts/design/vetorizar.py caminho/do/logo.png [--pb]   (--pb = preto e branco)"""
import sys
from pathlib import Path
import vtracer

entrada = Path(sys.argv[1])
saida = entrada.with_suffix(".svg")
modo = "binary" if "--pb" in sys.argv else "color"
vtracer.convert_image_to_svg_py(str(entrada), str(saida), colormode=modo, mode="spline", filter_speckle=4)
print(f"Vetor salvo em {saida}")
