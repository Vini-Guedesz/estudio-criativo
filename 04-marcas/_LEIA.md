# 04-marcas: tudo de cada marca num lugar só

> Data: 2026-10-25 · Tipo: entrada · Status: vigente

**Resumo:** cada marca tem uma pasta, e tudo dela fica dentro: identidade, referências, modelos e todas as peças (reels, posts, carrosséis, stories e vídeos). Toda peça segue o mesmo padrão de pastas e de nomes, com `rascunhos/` e `final/`. As pastas são criadas pelo `scripts/peca.py`. Não crie peça, rascunho ou entrega fora deste padrão.

## A estrutura

```
04-marcas/
├── _modelo-marca/                 ← cópia limpa para cada marca nova (não mexa)
├── _modelo-peca/README.md         ← ficha de cada peça nova (não mexa)
└── <marca>/                       ← ex.: cafe-do-ze
    ├── README.md                  ← ficha da marca
    ├── calendario.md              ← pilares, ritmo e plano de publicação (skill redes-sociais)
    ├── resultados.md              ← números de cada peça, médias da conta, relatórios do mês
    ├── identidade/
    │   ├── briefing.md            ← entrevista da marca (setup/4-marca.md)
    │   ├── plataforma.md          ← posicionamento, personalidade, voz
    │   ├── design-tokens/
    │   │   ├── marca.json         ← fonte única de cores e fontes
    │   │   └── saida/             ← marca.css e marca.json gerados (npm run tokens)
    │   ├── direcoes/              ← provas das direções visuais propostas (post e capa de Reels de cada uma)
    │   ├── logo/                  ← SVG mestre e PNGs; logo/conceitos/ guarda as rodadas; logo/otimizado/ sai do npm run svg
    │   └── avatar/
    ├── referencias/               ← referências só desta marca: mural.md (links), analises/ e a mídia por categoria
    ├── modelos/                   ← modelos reutilizáveis: post, abertura, vinheta, lower third
    ├── reels/                     ← vídeo vertical curto
    ├── videos/                    ← vídeo longo (YouTube etc.)
    ├── stories/
    ├── posts/                     ← post único do feed
    └── carrosseis/
```

## Toda peça, sempre igual

Uma pasta por peça, dentro do tipo dela: `04-marcas/<marca>/<tipo>/AAAA-MM-DD-tema/`. A data é a do início da peça e o tema vai sem acento, em minúsculas, com hífen.

```
04-marcas/cafe-do-ze/reels/2026-10-25-lancamento/
├── README.md       ← ficha: ideia, critério de pronto, checklist, entregas
├── copy.md         ← ganchos, texto da tela, legenda, hashtags, CTA (skill copy-redes)
├── roteiro.md      ← (vídeo) estrutura (IA) e texto final (dono)
├── referencias/    ← referências e assets citados só nesta peça + FONTES.md
├── assets/         ← prints, fotos, logos, gravações de tela usados na peça
├── audio/          ← (vídeo) narração aprovada, trilha, eventos.json, mix
├── motor/          ← (vídeo) projeto do After Effects, EffectCraft, HyperFrames ou Remotion
├── revisao/        ← (vídeo) quadros, comparações, notas
├── rascunhos/      ← toda prévia e versão: v1, v2, v3...
└── final/          ← só o que foi aprovado, pronto para publicar
```

Post e carrossel recebem só `README.md`, `copy.md`, `referencias/`, `assets/`, `rascunhos/` e `final/`.

## Nomes dos arquivos

| Onde | Padrão | Exemplo |
|---|---|---|
| `rascunhos/` | `<tema>-<tipo>-v<N>.<ext>` | `lancamento-reels-v3.mp4` |
| `rascunhos/` (carrossel) | `<tema>-carrossel-v<N>-<tela>.png` | `5-erros-carrossel-v2-01.png` |
| `rascunhos/` (extras) | `<tema>-<tipo>-<extra>-v<N>.<ext>` | `lancamento-reels-legenda-v2.txt`, `lancamento-reels-capa-v1.png` |
| `final/` | `<tema>-<tipo>.<ext>` | `lancamento-reels.mp4`, `5-erros-carrossel-01.png` |
| `final/` (extras) | `<tema>-<tipo>-<extra>.<ext>` | `lancamento-reels-capa.png`, `lancamento-reels-legenda.txt` (texto do post), `lancamento-reels-legendas.srt` (legendas do vídeo) |

O tipo no nome do arquivo vai no singular: `reels`, `video`, `story`, `post`, `carrossel`. Nada de `post-1729876543.png`, `final2.mp4` ou `render-novo.mp4`.

## Comandos

Todos rodam da raiz do estúdio.

| Comando | Faz |
|---|---|
| `uv run scripts/peca.py marca "Nome da Marca"` | cria `04-marcas/nome-da-marca/` a partir do modelo |
| `uv run scripts/peca.py renomear "Nome Novo"` | troca o nome da marca (pasta, caminhos nos documentos e título da ficha) |
| `uv run scripts/peca.py nova reels "Lançamento"` | cria a peça com as pastas certas (tipos: `reels`, `videos`, `stories`, `posts`, `carrosseis`) |
| `uv run scripts/peca.py rascunho <peça> mp4` | diz o caminho do próximo rascunho: renderize direto nele. `--extra legenda` (ou `capa`, `miniatura`) para os complementares, com versão própria |
| `uv run scripts/peca.py aprovar <rascunho>` | copia para `final/` com o nome limpo e anota em "Entregas" no README da peça |
| `uv run scripts/peca.py lista` | mostra as marcas e as peças |
| `npm run post --prefix scripts/design -- --peca <peça> "Título" "apoio"` | post 1080x1350 com a identidade da marca (fonte, cores por contraste, logo), salvo em `rascunhos/` da peça. Layouts `capa`, `conteudo` e `cta` |

Com uma marca só, ninguém precisa dizer qual é. Com mais de uma, passe `--marca <nome>`. `<peça>` pode ser o caminho ou só o nome da pasta (`2026-10-25-lancamento`).

## Regras

- **Render e exportação vão direto para `rascunhos/`**, com o nome que o `peca.py rascunho` der. Isso vale para todo motor: After Effects, EffectCraft, HyperFrames, Remotion, post e qualquer imagem gerada.
- **`final/` só recebe arquivo aprovado pelo dono**, e sempre pelo `peca.py aprovar`. Mudou depois de aprovado? Faça uma versão nova em `rascunhos/` e aprove de novo: o final é substituído.
- **Referência que serve a várias marcas** vai para `03-referencias/`. A que é só desta marca vai para `<marca>/referencias/`, e a que é só de uma peça vai para `referencias/` da peça.
- **Nada da marca fora da pasta dela.** Logo, cores, fontes compradas para ela, modelos e peças: tudo dentro de `04-marcas/<marca>/`. Música, efeitos e fontes de uso geral ficam em `05-biblioteca/`.
- **No git:** `rascunhos/` e `identidade/design-tokens/saida/` ficam fora. Vídeo e áudio ficam fora em qualquer pasta (`.gitignore` da raiz). A mídia das referências também fica fora: só os `.md` entram.
