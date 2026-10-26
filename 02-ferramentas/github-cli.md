# GitHub CLI (gh)

> Data: 2026-10-24 · Tipo: guia · Status: vigente

**Resumo:** ferramenta de terminal do GitHub. Usamos para criar repositórios e publicar a pasta sem abrir o site.

- **Como acessar:** comando `gh` no terminal (instalado em `C:\Program Files\GitHub CLI\`; terminais abertos antes da instalação precisam ser reabertos para achar o comando).
- **Instalação:** `winget install --id GitHub.cli -e`.
- **Credenciais:** login feito com `gh auth login` (navegador); o token fica guardado pelo próprio gh, nunca em arquivo da pasta.
- **Comandos mais usados:** `gh auth status` · `gh repo create estudio-criativo --private --source . --push` · `gh repo view --web`
- **Pegadinhas:** sem login, todo comando que fala com o GitHub falha com "not logged into any GitHub hosts".
- **Log:** 2026-10-24, instalado v2.103.2 para publicar o modelo do estúdio.
