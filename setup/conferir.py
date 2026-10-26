"""Confere o que está instalado no estúdio e grava 02-ferramentas/inventario.md.

    uv run setup/conferir.py            (relatório)
    uv run setup/conferir.py --estrito  (sai com erro se faltar algo essencial; usado no teste automático)

Não instala nada: só olha. Rode depois do instalador, ou quando algo parar de funcionar.
"""
from __future__ import annotations

import datetime as dt
import importlib
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
HOME = Path.home()
WINDOWS = os.name == "nt"

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def rodar(*cmd: str, timeout: int = 30) -> tuple[int, str]:
    exe = shutil.which(cmd[0])
    if not exe:
        return 127, ""
    try:
        p = subprocess.run([exe, *cmd[1:]], capture_output=True, text=True, timeout=timeout,
                           encoding="utf-8", errors="replace")
        return p.returncode, (p.stdout or p.stderr).strip()
    except Exception as e:  # noqa: BLE001 — conferência nunca quebra
        return 1, str(e)


def versao(*cmd: str) -> str | None:
    cod, saida = rodar(*cmd)
    if cod != 0 or not saida:
        return None
    return saida.splitlines()[0][:60]


linhas: list[tuple[str, str, bool, str, bool]] = []  # grupo, nome, ok, detalhe, essencial


def item(grupo: str, nome: str, ok: bool, detalhe: str = "", essencial: bool = False) -> None:
    linhas.append((grupo, nome, ok, detalhe, essencial))


# Programas ------------------------------------------------------------------
for nome, cmd, essencial in [
    ("Git", ("git", "--version"), True),
    ("Node.js", ("node", "--version"), True),
    ("npm", ("npm", "--version"), True),
    ("FFmpeg", ("ffmpeg", "-version"), True),
    ("FFprobe", ("ffprobe", "-version"), True),
    ("uv", ("uv", "--version"), True),
    ("Claude Code", ("claude", "--version"), False),
    ("Codex", ("codex", "--version"), False),
    ("ai-memory", ("ai-memory", "--version"), False),
]:
    v = versao(*cmd)
    item("Programas", nome, v is not None, v or "não encontrado", essencial)

if not (shutil.which("claude") or shutil.which("codex")):
    item("Programas", "Uma IA (Claude Code ou Codex)", False, "instale pelo menos uma", True)

# Bibliotecas Python -----------------------------------------------------------
for mod, nome, essencial in [
    ("numpy", "numpy", True), ("scipy", "scipy", True), ("soundfile", "soundfile", True),
    ("librosa", "librosa", True), ("pyloudnorm", "pyloudnorm", True), ("pedalboard", "pedalboard", False),
    ("faster_whisper", "faster-whisper", True), ("cv2", "opencv", True), ("PIL", "Pillow", True),
    ("playwright", "playwright", False), ("yt_dlp", "yt-dlp", True),
    ("torch", "torch (IA de áudio)", False), ("beat_this", "beat_this (batidas)", False),
    ("audio_separator", "audio-separator (voz e instrumental)", False),
]:
    try:
        m = importlib.import_module(mod)
        det = getattr(m, "__version__", "") or "ok"
        if mod == "torch":
            det += " · CUDA" if m.cuda.is_available() else (
                " · chip Apple (MPS)" if getattr(m.backends, "mps", None) and m.backends.mps.is_available() else " · processador")
        item("Python", nome, True, str(det)[:60], essencial)
    except Exception:  # noqa: BLE001
        dica = "uv sync --extra cpu (ou gpu)" if mod in ("torch", "beat_this", "audio_separator") else "uv sync"
        item("Python", nome, False, f"falta: {dica}", essencial)

chromium = list((HOME / ("AppData/Local/ms-playwright" if WINDOWS else (
    "Library/Caches/ms-playwright" if sys.platform == "darwin" else ".cache/ms-playwright"))).glob("chromium*"))
item("Python", "Chromium do Playwright", bool(chromium), "ok" if chromium else "uv run playwright install chromium")

# Skills -----------------------------------------------------------------------
locais = sorted(s.parent.name for s in (RAIZ / ".agents" / "skills").glob("*/SKILL.md"))
item("Skills", "Skills do estúdio", bool(locais), ", ".join(locais) or "nenhuma em .agents/skills", True)
item("Skills", "Ligação .claude/skills", (RAIZ / ".claude" / "skills").exists(),
     "ok" if (RAIZ / ".claude" / "skills").exists() else "rode o instalador de novo")
pastas_globais = [HOME / ".claude" / "skills", HOME / ".agents" / "skills"]
for nome, alvo in [("HyperFrames", "hyperframes"), ("Remotion", "remotion-best-practices"),
                   ("Transições", "transitions-dev"), ("watch (assistir vídeo)", "watch"),
                   ("humanizer", "humanizer")]:
    achou = any((p / alvo).exists() for p in pastas_globais)
    item("Skills", nome, achou, "ok" if achou else "npx skills add ... (veja setup/2-instalar.md)")

# Motores de vídeo -------------------------------------------------------------
cod, saida = rodar("claude", "mcp", "list", timeout=60) if shutil.which("claude") else (1, "")
mcps = saida.lower()
if WINDOWS:
    ec = [p for base in (Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "EffectCraft",
                         Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "EffectCraft")
          for p in base.rglob("effectcraft-cli.exe")] if os.environ.get("LOCALAPPDATA") else []
    ae = sorted(Path(os.environ.get("ProgramFiles", "C:/Program Files"), "Adobe").glob("Adobe After Effects*/Support Files/AfterFX.exe"))
else:
    ec = list((HOME / "Applications" / "EffectCraft").rglob("effectcraft-cli"))
    ae = sorted(Path("/Applications").glob("Adobe After Effects*"))
item("Motores", "EffectCraft", bool(ec), str(ec[0].parent) if ec else "rode o instalador (passo 6)")
item("Motores", "EffectCraft no Claude Code", "effectcraft" in mcps, "MCP effectcraft" if "effectcraft" in mcps else "não registrado")
item("Motores", "After Effects", bool(ae), ae[-1].parts[-3] if ae and WINDOWS else (ae[-1].name if ae else "opcional"))
item("Motores", "HyperFrames e Remotion", bool(shutil.which("npx")), "rodam por npx dentro de cada projeto")

# Design e identidade visual ----------------------------------------------------
for mod, nome in [("vtracer", "vtracer (PNG → SVG)"), ("rembg", "rembg (remover fundo)"),
                  ("coloraide", "coloraide (cores e contraste)"), ("colorthief", "colorthief (paleta)"),
                  ("drawsvg", "drawsvg"), ("fontTools", "fonttools")]:
    try:
        importlib.import_module(mod)
        item("Design", nome, True, "ok")
    except Exception:  # noqa: BLE001
        item("Design", nome, False, "falta: uv sync --extra design")
nm = RAIZ / "scripts" / "design" / "node_modules"
item("Design", "Ferramentas Node (posts, avatar, tokens)", (nm / "satori").exists(),
     "ok" if (nm / "satori").exists() else "npm install dentro de scripts/design")
if WINDOWS:
    lad = Path(os.environ.get("LOCALAPPDATA", ""))
    ink = shutil.which("inkscape") or next(iter(Path(os.environ.get("ProgramFiles", "C:/Program Files"), "Inkscape", "bin").glob("inkscape.exe")), None)
    pc = list((lad / "Programs" / "PhotoCraft").rglob("photocraft-cli.exe")) if (lad / "Programs" / "PhotoCraft").exists() else []
    extras = {"Figma": lad / "Figma", "Krita": Path(os.environ.get("ProgramFiles", "C:/Program Files"), "Krita (x64)"),
              "DaVinci Resolve": Path(os.environ.get("ProgramFiles", "C:/Program Files"), "Blackmagic Design", "DaVinci Resolve")}
else:
    ink = shutil.which("inkscape") or (Path("/Applications/Inkscape.app") if Path("/Applications/Inkscape.app").exists() else None)
    pc = [a for a in (Path("/Applications/PhotoCraft.app"), HOME / "Applications" / "PhotoCraft.app") if a.exists()]
    extras = {"Figma": Path("/Applications/Figma.app"), "Krita": Path("/Applications/krita.app"),
              "DaVinci Resolve": Path("/Applications/DaVinci Resolve")}
item("Design", "Inkscape", bool(ink), str(ink) if ink else "rode o instalador (passo 6b)")
item("Design", "PhotoCraft", bool(pc), str(pc[0].parent) if pc else "rode o instalador (passo 6b)")
mcp_local = (RAIZ / ".mcp.json").read_text(encoding="utf-8") if (RAIZ / ".mcp.json").exists() else ""
item("Design", "PhotoCraft no Claude Code", "photocraft" in mcp_local, "MCP photocraft (.mcp.json)" if "photocraft" in mcp_local else "não registrado")
for nome, caminho in extras.items():
    item("Design", nome, caminho.exists(), "ok" if caminho.exists() else "opcional (-AppsDesign / --apps-design)")
for nome, alvo in [("Skill canvas-design", "canvas-design"), ("Skill theme-factory", "theme-factory")]:
    achou = any((pp / alvo).exists() for pp in pastas_globais)
    item("Design", nome, achou, "ok" if achou else "npx skills add anthropics/skills ...")

# Segundo cérebro --------------------------------------------------------------
perfil = RAIZ / "01-sobre-mim" / "perfil.md"
perfil_ok = perfil.exists() and "PERFIL-EM-BRANCO" not in perfil.read_text(encoding="utf-8")
item("Cérebro", "Perfil preenchido", perfil_ok, "ok" if perfil_ok else "roteiro 1 (setup/1-segundo-cerebro.md)")
marcador = RAIZ / ".ai-memory.toml"
item("Cérebro", "Projeto no ai-memory", marcador.exists(), "ok" if marcador.exists() else "roteiro 1")
onde = (RAIZ / "03-referencias" / "ONDE.md").read_text(encoding="utf-8") if (RAIZ / "03-referencias" / "ONDE.md").exists() else ""
item("Cérebro", "Pasta de referências", "AAAA-MM-DD" not in onde, "ok" if "AAAA-MM-DD" not in onde else "roteiro 3 (setup/3-referencias.md)")
marcas = [m for m in (RAIZ / "04-marcas").glob("*") if m.is_dir() and not m.name.startswith(("_", "."))]
prontas = [m.name for m in marcas if (m / "identidade" / "briefing.md").exists()
           and "BRIEFING-EM-BRANCO" not in (m / "identidade" / "briefing.md").read_text(encoding="utf-8")]
item("Cérebro", "Marca com briefing", bool(prontas), ", ".join(prontas) if prontas else "roteiro 4 (setup/4-marca.md)")
sfx = list((RAIZ / "05-biblioteca" / "som" / "sfx").rglob("*.wav"))
item("Cérebro", "Efeitos sonoros", bool(sfx), f"{len(sfx)} arquivos" if sfx else "uv run scripts/som/sintetizar_sfx.py")

# Referências --------------------------------------------------------------------
mural = RAIZ / "03-referencias" / "mural.md"
item("Referências", "Mural de links", mural.exists(), "03-referencias/mural.md" if mural.exists() else "falta o 03-referencias/mural.md do modelo")
fichas = [f for f in (RAIZ / "03-referencias" / "estilos").glob("*.md") if not f.name.startswith("_")]
item("Referências", "Fichas de estilo", bool(fichas), f"{len(fichas)} fichas" if fichas else "falta a pasta 03-referencias/estilos do modelo")
for nome_skill in ("copy-redes", "redes-sociais", "referencias-e-estilos"):
    achou = (RAIZ / ".agents" / "skills" / nome_skill / "SKILL.md").exists()
    item("Referências", f"Skill {nome_skill}", achou, "ok" if achou else "falta em .agents/skills")

# Marcas: o estado de cada uma ---------------------------------------------------
import json  # noqa: E402
import re  # noqa: E402

for m in marcas:
    g = f"Marca {m.name}"
    ident = m / "identidade"
    br = ident / "briefing.md"
    item(g, "Briefing", br.exists() and "BRIEFING-EM-BRANCO" not in br.read_text(encoding="utf-8"),
         "ok" if m.name in prontas else "roteiro 4 (entrevista)")
    try:
        tk = json.loads((ident / "design-tokens" / "marca.json").read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        item(g, "Tokens (marca.json)", False, f"não li o marca.json: {e.__class__.__name__}")
        continue
    item(g, "Tokens definidos", "_modelo" not in tk, "ok" if "_modelo" not in tk else "ainda com os valores do modelo (roteiro 4, passo 4)")
    estilo = tk.get("estilo", {}).get("value", "")
    ficha_ok = (RAIZ / "03-referencias" / "estilos" / f"{estilo}.md").exists()
    item(g, "Estilo dos posts", ficha_ok, estilo if ficha_ok else f"'{estilo or 'vazio'}' não tem ficha em 03-referencias/estilos")
    for papel, rotulo in (("titulo", "Fonte dos títulos"), ("texto", "Fonte do texto")):
        fam = tk.get("fonte", {}).get(papel, {}).get("value", "Inter")
        s = re.sub(r"[^a-z0-9]+", "-", fam.lower()).strip("-")
        inst = (nm / "@fontsource" / s).exists()
        item(g, rotulo, inst, fam if inst else f"{fam}: npm install @fontsource/{s} --prefix scripts/design")
    css = ident / "design-tokens" / "saida" / "marca.css"
    item(g, "Tokens exportados (CSS)", css.exists(), "ok" if css.exists() else f"npm run tokens --prefix scripts/design -- --marca {m.name}")
    logos = list((ident / "logo").glob("*.svg")) if (ident / "logo").exists() else []
    item(g, "Logo", bool(logos), f"{len(logos)} SVG" if logos else "ainda sem logo em identidade/logo/")
    cal = m / "calendario.md"
    plano = cal.exists() and re.search(r"^\| \d{4}-\d{2}-\d{2} \|", cal.read_text(encoding="utf-8"), re.M)
    item(g, "Calendário", bool(plano), "com peças planejadas" if plano else "vazio (skill redes-sociais)")

# Saída -------------------------------------------------------------------------
faltam_essenciais = [n for _, n, ok, _, e in linhas if e and not ok]
agora = dt.datetime.now()
md = [
    "# Inventário do estúdio",
    "",
    f"> Data: {agora:%Y-%m-%d} · Tipo: dados · Status: vigente",
    "",
    f"**Como usar:** gerado por `uv run setup/conferir.py` em {agora:%d/%m/%Y %H:%M} "
    f"({platform.system()} {platform.release()}, {platform.machine()}). Não edite à mão: rode o script de novo.",
    "",
    "| Grupo | Item | Pronto | Detalhe |",
    "|---|---|---|---|",
]
grupo_anterior = None
print()
for grupo, nome, ok, det, essencial in linhas:
    if grupo != grupo_anterior:
        print(f"\n{grupo}")
        grupo_anterior = grupo
    marca = "ok" if ok else ("FALTA" if essencial else "--")
    print(f"  {marca:>5}  {nome:<38} {det}")
    md.append(f"| {grupo} | {nome} | {'sim' if ok else ('**falta**' if essencial else 'não')} | {det.replace('|', '/')} |")

md += ["", "## Resultado", "",
       "Tudo o que é essencial está pronto." if not faltam_essenciais
       else "Falta o essencial: " + ", ".join(faltam_essenciais) + "."]
(RAIZ / "02-ferramentas").mkdir(exist_ok=True)
(RAIZ / "02-ferramentas" / "inventario.md").write_text("\n".join(md) + "\n", encoding="utf-8")

print()
if faltam_essenciais:
    print("Falta o essencial: " + ", ".join(faltam_essenciais))
    if "--estrito" in sys.argv:
        sys.exit(1)
else:
    print("Essencial pronto. Itens marcados com -- são opcionais.")
