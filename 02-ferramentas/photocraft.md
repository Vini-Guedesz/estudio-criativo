# PhotoCraft

> Data: 2026-10-24 · Tipo: guia · Status: vigente

**Resumo:** editor de imagem gratuito e open source (alternativa ao Photoshop, em alpha). Usamos para tratar fotos, mockups e abrir/salvar `.psd`.

- **Como acessar:** app (Menu Iniciar > PhotoCraft), CLI `photocraft-cli.exe` e MCP `photocraft` (configurado em `.mcp.json`, só lê e grava dentro desta pasta).
- **Instalação:** passo 6b do instalador. Windows: zip portátil de github.com/storytold/photocraft em `%LOCALAPPDATA%\Programs\PhotoCraft\`, e o `.mcp.json` (fora do git) é gerado para a pasta do projeto; se a pasta for renomeada, troque os dois caminhos `--automation-*-root` nele e reabra o Claude. Mac: `.dmg` do mesmo endereço.
- **Credenciais:** nenhuma.
- **Comandos mais usados:** `photocraft-cli convert entrada.png saida.psd` · `photocraft-cli info arquivo.psd` · `photocraft-cli batch --actions acoes.atn --in pasta --out saida`
- **Pegadinhas:** alpha; sem preenchimento generativo por IA; tipografia fraca (texto de post: preferir Figma ou `npm run post`). Para atualizar: apagar a pasta do PhotoCraft e rodar o instalador de novo.
- **Log:** 2026-10-24, instalado v0.15.1, teste de conversão PNG→PSD ok. 2026-10-24, `.mcp.json` apontado para a pasta renomeada `estudio-criativo`.
