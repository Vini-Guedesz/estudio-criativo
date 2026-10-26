---
name: referencias-e-estilos
description: Pontapé inicial de uma marca ou de uma peça a partir das referências - ler o mural de links (Reels, vídeos, imagens, perfis, sites), baixar e analisar cada um, identificar o estilo visual (pixel art, neobrutalismo, glassmorfismo, Y2K, colagem e as outras fichas de 03-referencias/estilos), montar a prancha e propor direções visuais. Usar quando a pessoa mandar links ou prints de referência, pedir "começa pelas referências", "qual é esse estilo?", "quero algo nesse estilo", ou quando uma marca ou peça nova ainda não tiver direção visual.
---

# Referências e estilos: o pontapé inicial

> Data: 2026-10-25 · Tipo: guia · Status: vigente

**Resumo:** como transformar os links que a pessoa salvou em uma direção visual concreta. Ler o mural, analisar cada referência, dar nome aos estilos com as fichas de `03-referencias/estilos/`, propor 2 ou 3 direções e registrar a escolha na marca ou na peça. Para vídeo com motion, a medição quadro a quadro continua na skill `video-referencias`.

## Onde as coisas ficam

| O quê | Onde |
|---|---|
| Links salvos, com o motivo e o status | `03-referencias/mural.md` (geral) e `04-marcas/<marca>/referencias/mural.md` (da marca) |
| Fichas de estilo | `03-referencias/estilos/` ([índice](../../../03-referencias/estilos/_LEIA.md)) |
| Mídia baixada e organizada | pasta do `03-referencias/ONDE.md` (geral) ou `04-marcas/<marca>/referencias/<categoria>/` (da marca) |
| Análise de cada referência | `03-referencias/analises/` (geral) ou `04-marcas/<marca>/referencias/analises/` (da marca) |
| A direção escolhida | marca: seção 8 do `identidade/briefing.md` e `identidade/plataforma.md`. Peça: `README.md` da peça e `06-metodo/escolhas.md` |

## O pontapé inicial

### 1. Juntar

1. Se a pessoa mandou links na conversa, coloque cada um no mural certo (geral ou da marca), na seção do tipo, com o motivo que ela disse e status `novo`.
2. Peça mais se houver menos de 5 referências: "manda de 5 a 10 links ou prints de coisas que você gostaria que a marca parecesse, e 2 ou 3 do que ela não pode parecer". As que ela não quer também entram no mural, com "NÃO:" no motivo.
3. Leia o catálogo (`rg -i "palavra" 03-referencias/catalogo.md`) e as fichas de estilo que a pessoa citou.

### 2. Baixar e olhar

1. `uv run scripts/referencias.py mural --baixar` (ou `--marca <marca> --baixar`) baixa os vídeos e imagens `novo` para a `_entrada/`.
2. O que não baixar (Instagram pedindo login, site bloqueando): peça um print ou gravação de tela para a `00-entrada/`, ou abra no navegador e capture.
3. Vídeo: `uv run scripts/referencias.py olhar <arquivo>` (folha de contato) e a skill `watch` para o áudio e a intenção. Imagem: abra e veja.
4. Perfis e sites: `uv run scripts/referencias.py capturar <url>` tira a tela no desktop e no celular (fecha o aviso de cookies). Em perfil, olhe os 9 a 12 posts mais recentes; em site, a página inicial e uma interna.

### 3. Analisar cada referência

Para cada uma, escreva uma análise curta (modelo abaixo). Referência que vai guiar uma peça de vídeo também recebe a medição de movimento da `video-referencias`.

```markdown
# <assunto>

> Data: AAAA-MM-DD · Tipo: análise · Status: vigente

**Resumo:** o que é e por que foi salva, em 1 ou 2 frases.

- **Origem:** <link> · **Marca:** <marca ou geral>
- **Estilo:** <ficha de estilos/> (dominante) + <apoio, se houver>
- **Cores:** hex principais (`uv run scripts/design/paleta.py <imagem>`)
- **Tipografia:** família parecida gratuita e como é usada (peso, caixa, tamanho)
- **Forma e composição:** grid, cantos, contorno, sombra, textura
- **Movimento** (vídeo): como entra, sai e transita; ritmo
- **Som** (vídeo): trilha e efeitos
- **O que levar:** o que vale para a marca ou a peça
- **O que não levar:** o que não combina com a voz da marca
```

Depois, mova a mídia e marque o mural:

- `uv run scripts/referencias.py mover <arquivo> <categoria> --tags "<estilo>, ..." --nota "..."` (acrescente `--marca <marca>` se for só da marca).
- No mural, troque o status para `analisado` e ponha o caminho da análise ao lado: `analisado · analises/AAAA-MM-DD-assunto.md`.

### 4. Dar nome aos estilos

1. Agrupe as referências pelos estilos das fichas. Quase sempre aparecem um ou dois estilos dominantes.
2. Leia a ficha de cada estilo dominante.
3. Referência que não cabe em nenhuma ficha: descreva o que ela tem e, se o estilo se repetir em 3 ou mais referências, crie a ficha nova a partir do `estilos/_modelo.md`.
4. Confronte com as referências "NÃO": se um estilo aparece nas duas listas, a diferença está num detalhe (cor, peso, ritmo). Diga qual.

### 5. Propor as direções

Proponha **2 ou 3 direções** diferentes de verdade. Cada uma com:

- **Nome** e uma frase de conceito.
- **Estilo:** dominante + apoio (ex.: clean tech com botões neobrutalistas).
- **Paleta** (hex), **fontes** (gratuitas), **forma** (cantos, contorno, sombra), **movimento** e **som**.
- **As referências do mural** que sustentam a direção.
- **Prova visual:** a mesma cena em cada direção para comparar com justiça. Para marca: um post e uma capa de Reels. Para vídeo: os mesmos 3 quadros do gancho e do corpo (o `video-do-zero` pede isso na etapa 6). Gere com o `npm run post --prefix scripts/design -- --estilo <ficha>`, com um HTML por direção renderizado por `uv run scripts/design/render.py <html> --tamanho post|reels --saida <png>`, ou com IA de imagem. Abra cada imagem e confira antes de mostrar. Provas de marca ficam em `04-marcas/<marca>/identidade/direcoes/`; provas de peça, em `revisao/` da peça.

A pessoa escolhe, mistura ou pede outra rodada com mais referências.

### 6. Registrar a escolha

- **Marca:** a direção vai para a seção 8 do `briefing.md`. Cores e fontes vão para o `identidade/design-tokens/marca.json` (e `npm run tokens --prefix scripts/design`), e o conceito para a `plataforma.md`. Segue o roteiro `setup/4-marca.md` (logo, avatar, posts).
- **Peça:** a direção vai para o `README.md` da peça (seção Decisões) e para o `06-metodo/escolhas.md` (o que estava na mesa, o que ganhou e por quê).
- Cite a peça final em "Exemplos salvos" da ficha do estilo usado.

## Regras

- **Referência é estudo, não cópia.** Leve estrutura, ritmo, tipo de composição e sensação. Logo, personagem, foto e texto dos outros não entram na peça.
- **A marca manda na paleta.** Quando a marca já tem cores, o estilo empresta forma, tipografia e movimento, e a cor se adapta.
- **Dois estilos no máximo** por direção: um dominante e um de apoio.
- **Toda referência analisada vira documento** (regra do `AGENTS.md`). O mural guarda o link. A análise guarda o que vimos, para ninguém precisar reabrir a fonte.
