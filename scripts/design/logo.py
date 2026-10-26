"""Logo da marca: monta a versão com nome (texto em curvas na fonte da marca), a foto de perfil e a folha de conceito.

O símbolo é desenhado à parte (SVG feito à mão, no Inkscape ou vetorizado com vetorizar.py). Este script junta
o símbolo com o nome, sem depender da fonte instalada no computador de quem abrir o arquivo.

Uso (da raiz do estúdio):
  uv run scripts/design/logo.py montar <simbolo.svg> --saida <arquivo.svg> [--nome "Sem Fila"] [--cidade "São Luís"]
        [--cor-texto #0B47A8] [--cor-cidade #16202E] [--peso 800] [--marca m]
  uv run scripts/design/logo.py perfil <simbolo.svg> --saida <arquivo.png> [--fundo #FFFFFF]
  uv run scripts/design/logo.py folha <simbolo.svg> --saida <folha.png> [--negativo <simbolo-negativo.svg>]
        [--titulo "1 · Nome do conceito"] [--ideia "a ideia em uma frase"] [--nome "Sem Fila"] [--marca m]

Variações de cor (negativo, uma cor escura, uma cor branca) são símbolos SVG próprios: monte cada um com
`montar`, trocando o símbolo e a --cor-texto. A fonte vem de fonte.titulo do marca.json da marca.
"""
from __future__ import annotations

import argparse
import base64
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from _estudio import fonte_da_marca, marca  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def tokens(pasta_marca: Path) -> dict:
    return json.loads((pasta_marca / "identidade" / "design-tokens" / "marca.json").read_text(encoding="utf-8"))


def cor(tk: dict, nome: str, padrao: str) -> str:
    return tk.get("cor", {}).get(nome, {}).get("value", padrao)


def nome_da_marca(pasta_marca: Path) -> str:
    leia = pasta_marca / "README.md"
    if leia.exists():
        primeira = leia.read_text(encoding="utf-8").splitlines()[0]
        if primeira.startswith("# "):
            return primeira[2:].strip()
    return pasta_marca.name


def caixa_do_svg(svg: str) -> tuple[float, float, float, float]:
    m = re.search(r'viewBox="\s*([-\d.]+)[\s,]+([-\d.]+)[\s,]+([-\d.]+)[\s,]+([-\d.]+)\s*"', svg)
    if m:
        return tuple(float(x) for x in m.groups())  # type: ignore[return-value]
    w = re.search(r'width="([\d.]+)', svg)
    h = re.search(r'height="([\d.]+)', svg)
    return (0, 0, float(w.group(1)) if w else 200, float(h.group(1)) if h else 200)


def simbolo_aninhado(svg: str, x: float, y: float, altura: float) -> tuple[str, float]:
    """O SVG do símbolo dentro de outro SVG, na altura pedida. Devolve (trecho, largura)."""
    vx, vy, vw, vh = caixa_do_svg(svg)
    largura = altura * vw / vh
    corpo = re.sub(r"^.*?<svg[^>]*>", "", svg, count=1, flags=re.S)
    corpo = re.sub(r"</svg>\s*$", "", corpo.strip())
    return (f'<svg x="{x:.1f}" y="{y:.1f}" width="{largura:.1f}" height="{altura:.1f}" '
            f'viewBox="{vx} {vy} {vw} {vh}">{corpo}</svg>', largura)


def texto_em_curvas(arq_fonte: Path, texto: str, tamanho: float, x0: float, base: float, rastreio: float = -0.02):
    """Path SVG do texto na fonte (linha de base em `base`). Devolve (d, largura)."""
    from fontTools.pens.svgPathPen import SVGPathPen
    from fontTools.pens.transformPen import TransformPen
    from fontTools.ttLib import TTFont

    fonte = TTFont(str(arq_fonte))
    cmap, glifos, upm = fonte.getBestCmap(), fonte.getGlyphSet(), fonte["head"].unitsPerEm
    esc, x, partes = tamanho / upm, 0.0, []
    for ch in texto:
        nome = cmap.get(ord(ch))
        if nome is None:
            print(f"aviso: a fonte não tem o caractere '{ch}'")
            continue
        caneta = SVGPathPen(glifos)
        glifos[nome].draw(TransformPen(caneta, (esc, 0, 0, -esc, x0 + x, base)))
        partes.append(caneta.getCommands())
        x += glifos[nome].width * esc + rastreio * tamanho
    return " ".join(partes), max(x - rastreio * tamanho, 0)


def cmd_montar(a):
    pasta = marca(a.marca)
    tk = tokens(pasta)
    svg_simbolo = Path(a.simbolo).read_text(encoding="utf-8")
    arq_fonte = fonte_da_marca(pasta, "titulo", a.peso)
    nome = a.nome or nome_da_marca(pasta)
    ALT = 200
    trecho, larg_simb = simbolo_aninhado(svg_simbolo, 0, 0, ALT)
    x = larg_simb + ALT * 0.15
    partes = [trecho]
    if a.cidade:
        tam = ALT * 0.48
        d1, l1 = texto_em_curvas(arq_fonte, f"{a.cidade} – ", tam, x, ALT * 0.64)
        d2, l2 = texto_em_curvas(arq_fonte, nome, tam, x + l1, ALT * 0.64)
        partes += [f'<path d="{d1}" fill="{a.cor_cidade or cor(tk, "texto", "#111111")}"/>',
                   f'<path d="{d2}" fill="{a.cor_texto or cor(tk, "primaria", "#111111")}"/>']
        largura = x + l1 + l2
    else:
        tam = ALT * 0.75
        d, l = texto_em_curvas(arq_fonte, nome, tam, x, ALT * 0.70)
        partes.append(f'<path d="{d}" fill="{a.cor_texto or cor(tk, "primaria", "#111111")}"/>')
        largura = x + l
    largura += ALT * 0.05
    saida = Path(a.saida)
    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {largura:.0f} {ALT}" '
                     f'width="{largura:.0f}" height="{ALT}">\n' + "\n".join(partes) + "\n</svg>\n", encoding="utf-8")
    print(f"logo salvo em {saida}")


def renderiza(html: str, largura: int, altura: int, saida: Path):
    from playwright.sync_api import sync_playwright

    saida.parent.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        nav = p.chromium.launch()
        pag = nav.new_page(viewport={"width": largura, "height": altura})
        pag.set_content(html, wait_until="networkidle")
        pag.evaluate("document.fonts.ready")
        pag.screenshot(path=str(saida))
        nav.close()
    print(f"imagem salva em {saida}")


def cmd_perfil(a):
    svg = Path(a.simbolo).read_text(encoding="utf-8").replace("<svg ", '<svg width="100%" height="100%" ', 1)
    html = (f'<html><body style="margin:0;width:1080px;height:1080px;background:{a.fundo};display:flex;'
            f'align-items:center;justify-content:center"><div style="width:640px;height:640px">'
            f'{svg}</div></body></html>')
    renderiza(html, 1080, 1080, Path(a.saida))


def cmd_folha(a):
    pasta = marca(a.marca)
    tk = tokens(pasta)
    s = Path(a.simbolo).read_text(encoding="utf-8").replace("<svg ", '<svg width="100%" height="100%" ', 1)
    neg = Path(a.negativo).read_text(encoding="utf-8").replace("<svg ", '<svg width="100%" height="100%" ', 1) if a.negativo else s
    fonte64 = base64.b64encode(fonte_da_marca(pasta, "titulo", 800).read_bytes()).decode()
    nome = a.nome or nome_da_marca(pasta)
    primaria, texto, escura = cor(tk, "primaria", "#111111"), cor(tk, "texto", "#111111"), cor(tk, "primaria-escura", cor(tk, "texto", "#111111"))
    caixa = lambda tam: f'style="width:{tam}px;height:{tam}px;flex:none"'  # noqa: E731
    html = f"""<html><head><style>
@font-face {{ font-family:'Marca'; src:url(data:font/woff;base64,{fonte64}) format('woff'); font-weight:800; }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ width:1800px; height:1100px; font-family:'Marca', sans-serif; background:#F7F8FC; color:{texto}; padding:70px; }}
h2 {{ font-size:44px; font-weight:800; }} .ideia {{ font-family:sans-serif; font-size:24px; color:#4A5568; margin:10px 0 36px; max-width:1400px; }}
.grade {{ display:grid; grid-template-columns:440px 1fr 1fr; grid-template-rows:400px 330px; gap:30px; }}
.c {{ background:#fff; border-radius:24px; padding:36px; display:flex; align-items:center; justify-content:center; min-width:0; }}
.nome {{ font-weight:800; color:{primaria}; letter-spacing:-1px; white-space:nowrap; }}
small {{ font-family:sans-serif; font-size:18px; color:#7A8399; display:block; text-align:center; margin-top:8px; }}
</style></head><body>
<h2>{a.titulo or "Conceito"}</h2><p class="ideia">{a.ideia or ""}</p>
<div class="grade">
<div class="c" style="grid-row:1/3"><div {caixa(360)}>{s}</div></div>
<div class="c" style="grid-column:2/4;gap:30px"><div {caixa(130)}>{s}</div><span class="nome" style="font-size:96px">{nome}</span></div>
<div class="c" style="flex-direction:column;align-items:flex-start;gap:28px">
<div style="display:flex;align-items:center;gap:18px"><div {caixa(60)}>{s}</div><span style="font-size:30px;white-space:nowrap;color:{texto}">São Luís – <span class="nome">{nome}</span></span></div>
<div style="display:flex;align-items:center;gap:18px"><div {caixa(60)}>{s}</div><span style="font-size:30px;white-space:nowrap;color:{texto}">Pindamonhangaba – <span class="nome">{nome}</span></span></div></div>
<div class="c" style="flex-direction:column;gap:24px">
<div style="display:flex;align-items:flex-end;gap:28px">
<div><div style="width:170px;height:170px;border-radius:50%;background:#fff;box-shadow:0 0 0 2px #DCE0EC;display:flex;align-items:center;justify-content:center"><div {caixa(120)}>{s}</div></div><small>perfil</small></div>
<div><div {caixa(64)}>{s}</div><small>64</small></div><div><div {caixa(32)}>{s}</div><small>32</small></div><div><div {caixa(20)}>{s}</div><small>20</small></div></div>
<div style="background:{escura};border-radius:18px;padding:16px 26px;display:flex;align-items:center;gap:14px"><div {caixa(56)}>{neg}</div><span class="nome" style="font-size:36px;color:#fff">{nome}</span></div>
</div></div></body></html>"""
    renderiza(html, 1800, 1100, Path(a.saida))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("montar", help="símbolo + nome (texto em curvas) num SVG")
    s.add_argument("simbolo"); s.add_argument("--saida", required=True)
    s.add_argument("--nome"); s.add_argument("--cidade"); s.add_argument("--cor-texto"); s.add_argument("--cor-cidade")
    s.add_argument("--peso", type=int, default=800); s.add_argument("--marca")
    s.set_defaults(f=cmd_montar)
    s = sub.add_parser("perfil", help="foto de perfil 1080x1080 em PNG")
    s.add_argument("simbolo"); s.add_argument("--saida", required=True); s.add_argument("--fundo", default="#FFFFFF")
    s.set_defaults(f=cmd_perfil)
    s = sub.add_parser("folha", help="folha de apresentação de um conceito de logo")
    s.add_argument("simbolo"); s.add_argument("--saida", required=True); s.add_argument("--negativo")
    s.add_argument("--titulo"); s.add_argument("--ideia"); s.add_argument("--nome"); s.add_argument("--marca")
    s.set_defaults(f=cmd_folha)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
