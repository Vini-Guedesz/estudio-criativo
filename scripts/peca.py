"""Marcas e peças no padrão do estúdio: cria as pastas, dá o nome de cada rascunho e aprova o final.

Tudo de uma marca fica em 04-marcas/<marca>/; cada peça em 04-marcas/<marca>/<tipo>/AAAA-MM-DD-tema/,
sempre com rascunhos/ e final/. O padrão completo está em 04-marcas/_LEIA.md.

Uso (da raiz do estúdio):
    uv run scripts/peca.py marca "Nome da Marca"            cria 04-marcas/nome-da-marca/ a partir do modelo
    uv run scripts/peca.py renomear "Nome Novo"             troca o nome da marca (pasta e caminhos nos documentos)
    uv run scripts/peca.py nova reels "Lançamento"          cria a peça (tipos: reels, videos, stories, posts, carrosseis)
    uv run scripts/peca.py rascunho <peça> mp4              diz o caminho do próximo rascunho (v1, v2...)
    uv run scripts/peca.py rascunho <peça> txt --extra legenda   idem para a legenda, a capa, a miniatura...
    uv run scripts/peca.py aprovar <rascunho>               copia para final/ com o nome limpo e anota no README
    uv run scripts/peca.py lista                            mostra as marcas e as peças

Com mais de uma marca, passe --marca <nome> em 'nova' e 'lista'.
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _estudio import (MARCAS, PASTAS_PECA, PASTAS_VIDEO, RAIZ, TIPOS, marca, marcas, nome_final,  # noqa: E402
                      peca, rascunho, slug, tipo)

MODELO_MARCA = MARCAS / "_modelo-marca"
MODELO_PECA = MARCAS / "_modelo-peca" / "README.md"
MODELO_COPY = MARCAS / "_modelo-peca" / "copy.md"


def rel(p: Path) -> str:
    try:
        return p.resolve().relative_to(RAIZ).as_posix()
    except ValueError:
        return str(p)


def cmd_marca(a):
    nome = " ".join(a.nome)
    destino = MARCAS / slug(nome)
    if destino.exists():
        sys.exit(f"erro: {rel(destino)} já existe")
    shutil.copytree(MODELO_MARCA, destino)
    hoje = dt.date.today().isoformat()
    for md in destino.rglob("*.md"):  # ficha, mural, calendário, resultados nascem com a data de hoje
        if md.name != "briefing.md":  # o briefing ganha a data quando a entrevista terminar
            md.write_text(md.read_text(encoding="utf-8").replace("NOME-DA-MARCA", nome).replace("AAAA-MM-DD", hoje),
                          encoding="utf-8")
    print(f"marca criada: {rel(destino)}/")
    print("próximo passo: a entrevista da marca (setup/4-marca.md) preenche identidade/briefing.md")


def cmd_renomear(a):
    antiga = marca(a.marca)
    nome = " ".join(a.nome)
    nova = MARCAS / slug(nome)
    if nova.exists():
        sys.exit(f"erro: {rel(nova)} já existe")
    shutil.move(str(antiga), str(nova))
    # caminhos citados nos documentos do estúdio (catálogo, murais, escolhas, fichas, anotações)
    velho, novo = f"04-marcas/{antiga.name}/", f"04-marcas/{nova.name}/"
    ignorar = {".git", "node_modules", ".venv", "__pycache__"}
    mudados = 0
    for arq in RAIZ.rglob("*"):
        if arq.suffix.lower() not in (".md", ".json", ".txt") or not arq.is_file() or ignorar & set(arq.parts):
            continue
        bruto = arq.read_bytes()  # bytes: preserva a quebra de linha original (CRLF ou LF)
        if velho.encode() in bruto:
            arq.write_bytes(bruto.replace(velho.encode(), novo.encode()))
            mudados += 1
    ficha = nova / "README.md"
    if ficha.exists():
        bruto = ficha.read_bytes().decode("utf-8")
        primeira, _, resto = bruto.partition("\n")
        if primeira.startswith("# "):
            fim = "\r" if primeira.endswith("\r") else ""
            ficha.write_bytes(f"# {nome}{fim}\n{resto}".encode("utf-8"))
    print(f"marca renomeada: {rel(antiga)}/ → {rel(nova)}/ ({mudados} documento(s) com o caminho atualizado)")
    print("falta: trocar o nome no texto do briefing e da plataforma, e rodar `npm run tokens --prefix scripts/design` de novo")


def cmd_nova(a):
    t = tipo(a.tipo)
    base = marca(a.marca)
    data = a.data or dt.date.today().isoformat()
    tema = " ".join(a.tema)
    pasta = base / t / f"{data}-{slug(tema)}"
    if pasta.exists():
        sys.exit(f"erro: {rel(pasta)} já existe")
    video = TIPOS[t][1]
    for d in PASTAS_PECA + (PASTAS_VIDEO if video else []):
        (pasta / d).mkdir(parents=True)
    ficha = (MODELO_PECA.read_text(encoding="utf-8").replace("Título da peça", tema)
             .replace("AAAA-MM-DD", data).replace("TIPO-DA-PECA", t))
    (pasta / "README.md").write_text(ficha, encoding="utf-8")
    texto = MODELO_COPY.read_text(encoding="utf-8").replace("Título da peça", tema).replace("AAAA-MM-DD", data)
    (pasta / "copy.md").write_text(texto, encoding="utf-8")
    if video:
        (pasta / "roteiro.md").write_text(
            f"# Roteiro: {tema}\n\n> Data: {data} · Tipo: roteiro · Status: rascunho\n\n"
            "**Resumo:** estrutura (IA) e texto final (dono) da fala.\n", encoding="utf-8")
    print(f"peça criada: {rel(pasta)}/")
    print(f"primeiro rascunho: {rel(rascunho(pasta, 'mp4' if video else 'png'))}")


def cmd_rascunho(a):
    pasta = peca(a.peca)
    print(rel(rascunho(pasta, a.ext, a.parte, a.mesma_versao, a.extra)))


def cmd_aprovar(a):
    for arq in a.arquivos:
        origem = Path(arq).resolve()
        if not origem.exists():
            sys.exit(f"erro: não achei {arq}")
        if origem.parent.name != "rascunhos":
            sys.exit(f"erro: {arq} não está na pasta rascunhos/ de uma peça")
        destino = nome_final(origem)
        destino.parent.mkdir(exist_ok=True)
        shutil.copy2(origem, destino)
        ficha = destino.parent.parent / "README.md"
        if ficha.exists():
            v = re.search(r"-v(\d+)", origem.name)
            linha = f"| v{v.group(1) if v else '?'} | final/{destino.name} | {dt.date.today().isoformat()} | aprovado de rascunhos/{origem.name} |\n"
            texto = ficha.read_text(encoding="utf-8")
            ficha.write_text(texto.rstrip("\n") + "\n" + linha, encoding="utf-8")
        print(f"aprovado: {rel(destino)}")


def cmd_lista(a):
    lista = [marca(a.marca)] if a.marca else marcas()
    if not lista:
        print("nenhuma marca ainda. Crie com: uv run scripts/peca.py marca \"Nome da marca\"")
    for m in lista:
        print(f"{m.name}/")
        for t in TIPOS:
            pecas = sorted(p for p in (m / t).glob("*") if p.is_dir())
            for p in pecas:
                finais = len([f for f in (p / "final").glob("*") if f.is_file()])
                print(f"  {t}/{p.name}   ({finais} no final/)")


def main():
    for fluxo in (sys.stdout, sys.stderr):
        if hasattr(fluxo, "reconfigure"):
            fluxo.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("marca", help="cria uma marca nova a partir do modelo")
    s.add_argument("nome", nargs="+")
    s.set_defaults(f=cmd_marca)
    s = sub.add_parser("renomear", help="troca o nome da marca e atualiza os caminhos nos documentos")
    s.add_argument("nome", nargs="+", help="o nome novo")
    s.add_argument("--marca", help="a marca atual (com uma marca só, não precisa)")
    s.set_defaults(f=cmd_renomear)
    s = sub.add_parser("nova", help="cria uma peça (reels, videos, stories, posts, carrosseis)")
    s.add_argument("tipo")
    s.add_argument("tema", nargs="+")
    s.add_argument("--marca")
    s.add_argument("--data", help="AAAA-MM-DD (padrão: hoje)")
    s.set_defaults(f=cmd_nova)
    s = sub.add_parser("rascunho", help="caminho do próximo rascunho da peça")
    s.add_argument("peca", help="pasta da peça (caminho ou só o nome, ex.: 2026-10-25-lancamento)")
    s.add_argument("ext", help="extensão: mp4, png, jpg...")
    s.add_argument("--parte", type=int, help="número da tela do carrossel (01, 02...)")
    s.add_argument("--mesma-versao", action="store_true", help="não sobe a versão (outras telas da mesma versão)")
    s.add_argument("--extra", help="arquivo complementar com versão própria: legenda, capa, miniatura...")
    s.set_defaults(f=cmd_rascunho)
    s = sub.add_parser("aprovar", help="copia o rascunho aprovado para final/ com o nome limpo")
    s.add_argument("arquivos", nargs="+")
    s.set_defaults(f=cmd_aprovar)
    s = sub.add_parser("lista", help="lista marcas e peças")
    s.add_argument("--marca")
    s.set_defaults(f=cmd_lista)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
