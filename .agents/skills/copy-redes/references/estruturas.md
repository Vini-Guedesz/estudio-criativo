# Estruturas: legenda, carrossel, roteiro curto, stories, bio e slogan

> Data: 2026-10-25 · Tipo: guia · Status: vigente

**Resumo:** os modelos de texto de cada tipo de peça, com a estrutura narrativa que serve de base. Preencha com a voz da marca e com informação real. Os campos entre colchetes são o que a IA pergunta ou deduz do briefing.

## As estruturas de base

Toda peça curta usa uma destas. Escolha pela intenção, não pelo hábito.

| Estrutura | Sequência | Quando |
|---|---|---|
| **Gancho, valor, CTA** | prende → entrega 1 a 3 pontos → pede uma ação | dica, tutorial curto, lista. A mais usada |
| **Problema, agitação, solução (PAS)** | a dor → por que ela piora ou custa caro → o caminho | produto ou serviço que resolve algo concreto |
| **Antes, depois, ponte** | como era → como ficou → o que mudou no meio | transformação, caso de cliente (real), processo |
| **Atenção, interesse, desejo, ação (AIDA)** | prende → explica → mostra o ganho → pede | lançamento, oferta |
| **Situação, complicação, pergunta, resposta (SCQA)** | o cenário que todos aceitam → o que complica → a pergunta que surge → a resposta | assunto que precisa de argumento: opinião, explicação, LinkedIn |
| **Micro-história** | personagem → conflito → virada → o que ficou | bastidor, história da marca, vídeo emocional |

Na micro-história, o cliente é o personagem e a marca ajuda a resolver o conflito. A marca não é a heroína.

## Legenda

```
[Linha 1: gancho ou continuação do gancho da arte, até ~125 caracteres]

[Corpo: 2 a 5 parágrafos curtos ou uma lista.
 O que a peça não coube na arte: contexto, o passo a passo, o porquê.]

[CTA: uma ação, a mesma da peça]

[Hashtags: 3 a 5, específicas do assunto (ver redes-sociais/references/plataformas.md)]
```

- Parágrafo de 1 a 3 linhas. Quebra de linha ajuda a ler no celular.
- Emoji com função (marcar item de lista, substituir uma palavra), no máximo um por parágrafo. Se a voz da marca não usa emoji, não use.
- Palavras que a pessoa buscaria (o assunto dito com todas as letras) ajudam a peça a aparecer na busca da rede.
- Legenda de Reels pode ser curta (gancho + CTA). Legenda de carrossel educativo pode ser longa.

## Carrossel

Formato 1080x1350 (4:5). De 5 a 10 telas costuma bastar. Uma ideia por tela.

| Tela | Papel | Texto |
|---|---|---|
| 1. Capa | gancho | título de até 8 palavras + subtítulo opcional + sinal de "passe" |
| 2. Contexto | por que importa | a dor ou a situação, em 1 ou 2 frases |
| 3 a N-2 | o conteúdo | um ponto por tela: título curto (número + ideia) e até ~25 palavras de apoio |
| N-1. Resumo | o que levar | os pontos em uma lista ou uma frase-síntese |
| N. CTA | a ação | uma ação só, com o verbo do objetivo (salvar, mandar, comentar a palavra) |

- A tela 2 decide se a pessoa continua. Ela precisa abrir uma pergunta que as próximas respondem.
- Cada tela deve ser compreensível sozinha (o algoritmo pode mostrar o carrossel a partir da tela 2).
- Elementos visuais vêm da identidade da marca (`identidade/design-tokens/`). Gere as telas com `npm run post --prefix scripts/design -- --peca <peça> --parte N` (a partir da 2ª tela, some `--mesma-versao`): `--layout capa` na tela 1, `--layout conteudo --numero N` nas do meio e `--layout cta` na última.

Registre no `copy.md`, tela a tela:

```markdown
## Telas
1. **Capa:** [título] / [subtítulo] · visual: [o que aparece]
2. **Contexto:** [texto] · visual: [...]
...
```

## Roteiro curto

Reels, TikTok e Shorts: 9:16, 1080x1920. Pense em **blocos visuais de 3 a 5 segundos**, cada um com um papel. O roteiro vai no `roteiro.md` da peça (a fala é do dono) e o texto da tela no `copy.md`.

```
[0-3 s] GANCHO
  Vê-se: [ação ou imagem do primeiro quadro]
  Lê-se: [texto na tela, até 8 palavras]
  Ouve-se: [fala ou som]

[3-8 s] CONTEXTO / PROBLEMA
  Vê-se: ...  Lê-se: ...  Ouve-se: ...

[8-N s] VALOR: 1 a 3 pontos, um bloco cada
  ...

[últimos 3-5 s] CTA
  Lê-se: [a ação]   Ouve-se: [a mesma ação]
```

- Uma mudança visual a cada poucos segundos (corte, zoom, elemento novo, texto novo). Em vídeo acima de 1 minuto, uma quebra de padrão a cada 10 a 15 s.
- O vídeo tem que ser entendido **sem som**. Escreva primeiro a versão muda (imagem + texto), depois a fala.
- Final que conecta com o começo ajuda o vídeo a ser revisto em loop.
- Daqui em diante o vídeo segue o [video-do-zero](../../../../06-metodo/video-do-zero.md) e a skill `estudio-video`.

## Stories

Sequência de 3 a 6 telas. Cada tela é entendida em 1 segundo.

| Tela | Papel | Recurso |
|---|---|---|
| 1 | gancho: pergunta ou imagem forte | texto grande |
| 2 | contexto ou problema | enquete ("isso acontece com você?") |
| 3 a N-1 | conteúdo, bastidor ou demonstração | vídeo curto, caixa de pergunta, quiz |
| N | CTA | link, "responde aqui", "manda DM com a palavra X" |

- Uma interação (enquete, quiz, caixa de pergunta) logo no começo da sequência faz a pessoa participar.
- Resposta da caixa de pergunta vira conteúdo: a melhor resposta volta como story ou vira Reels.
- Story que funcionou vai para um destaque do perfil (ver bio, abaixo).

## Vídeo longo

YouTube e vídeos acima de 1 minuto. O método completo está no `video-do-zero`. A estrutura do texto:

1. **Gancho e promessa** (até 15 s): o que a pessoa vai saber ou ter no fim.
2. **Contexto** (curto): por que confiar e por que importa agora.
3. **Partes** (3 a 5): uma ideia por parte, com exemplo ou demonstração. Cada parte abre com uma frase que diz o que vem.
4. **Resumo**: os pontos em uma frase cada.
5. **CTA**: o próximo vídeo, a playlist ou a ação. No início, um pedido rápido no máximo.

Título com a palavra que a pessoa buscaria logo no começo. Descrição com 2 ou 3 frases sobre o vídeo e os capítulos com tempo.

## Bio

Instagram e TikTok: poucas linhas, lidas em 3 segundos.

```
[Nome de exibição: nome da marca + a palavra que a pessoa buscaria, ex.: "Ateliê Lua | Bolos de festa"]
[Linha 1: o que a marca faz e para quem]
[Linha 2: o diferencial ou a prova (real)]
[Linha 3: o que a pessoa ganha clicando no link]
[Link]
```

- Destaques: de 4 a 6, com nomes curtos e capas na identidade da marca. Exemplos: "Comece aqui", "Cardápio", "Clientes", "Bastidor", "Dúvidas".
- LinkedIn e site: três parágrafos. Quem é e o que faz, o que já entregou (com resultado real), como falar com você.

## Slogan

Uma frase curta (até 6 palavras) que a marca pode usar por anos. Gere de 10 a 15 opções em linhas diferentes, filtre para 5 e mostre:

| Linha | Estrutura | Exemplo |
|---|---|---|
| Benefício | verbo + o que a pessoa ganha | "Festa pronta, você presente" |
| Dor resolvida | menos [dor], mais [ganho] | "Menos dor, mais movimento" |
| Diferencial | o que só a marca tem | "Feito na hora, todo dia" |
| Propósito | o que a marca acredita | "Doce de verdade" |
| Jogo de palavras | só se a voz da marca for leve | |

Régua: fácil de falar, não lembra um concorrente, a marca consegue cumprir, funciona sem explicação. A escolha vai para a seção 8 do `briefing.md` da marca.
