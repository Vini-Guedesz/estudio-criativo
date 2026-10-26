---
name: copy-redes
description: Texto de redes sociais de uma marca do estúdio - gancho, legenda, texto das telas do carrossel, roteiro curto de Reels/TikTok/Shorts, sequência de stories, CTA, hashtags, bio do perfil, slogan e guia de voz da marca. Usar sempre que o pedido envolver escrever, revisar ou dar opções de texto para post, carrossel, reels, story ou perfil, ou definir como a marca fala.
---

# Copy de redes: o texto de cada peça

> Data: 2026-10-25 · Tipo: guia · Status: vigente

**Resumo:** como o estúdio escreve gancho, legenda, carrossel, roteiro curto, stories, CTA, bio e slogan, sempre na voz da marca e com o texto final aprovado pelo dono. O texto de cada peça fica no `copy.md` dela. Os modelos estão em [references/estruturas.md](references/estruturas.md), os ganchos em [references/ganchos.md](references/ganchos.md) e o guia de voz em [references/voz-da-marca.md](references/voz-da-marca.md).

## Antes de escrever

1. **Leia a marca.** `04-marcas/<marca>/identidade/briefing.md` (público, dores, palavras proibidas) e `identidade/plataforma.md` (voz, faça / não faça, pilares). Se não houver plataforma, monte o guia de voz primeiro ([references/voz-da-marca.md](references/voz-da-marca.md)).
2. **Abra a peça** (`uv run scripts/peca.py nova <tipo> "tema"`). Todo texto vai para o `copy.md` dela. Nada de texto solto na conversa sem registro.
3. **Combine três coisas em uma pergunta**, se o pedido não disser: para quem é, o que a pessoa deve fazer depois de ver (o CTA) e onde vai ser publicado.

## As regras

- **O texto final é do dono.** A IA propõe estrutura e opções (3 ganchos, 2 legendas). O dono escolhe, mistura ou reescreve. Fala gravada nunca é reescrita pela IA: no máximo ela aponta erro ou trecho confuso (igual ao roteiro no [video-do-zero](../../../06-metodo/video-do-zero.md)).
- **Nada inventado.** Número, porcentagem, depoimento, "mais de 500 clientes": só se vier do dono ou de fonte citada no `copy.md`. Sem dado real, escreva sem o número. Prova social falsa é o jeito mais rápido de queimar a marca.
- **Promessa que a peça cumpre.** O gancho promete o que o conteúdo entrega. Curiosidade sem entrega é isca, e quem cai uma vez não para de novo.
- **Um CTA por peça.** Uma ação só, dita com o verbo certo para o objetivo (tabela abaixo).
- **Escreva como a marca fala.** Use a voz da `plataforma.md`. Depois do rascunho, passe a skill `humanizer`: tire frases de efeito vazias, "não é X, é Y", tríades forçadas, travessões em excesso, palavras infladas e emoji em toda linha.
- **Específico ganha de genérico.** "3 erros na hora de precificar bolo de pote" funciona; "dicas de marketing" não. Cada frase tem que carregar uma informação.
- **Pense sem som.** Em vídeo curto, a mensagem principal precisa estar no texto da tela. A narração reforça.

## O que cada peça precisa

| Peça | O que escrever | Modelo |
|---|---|---|
| Post único | texto da arte (título + apoio curto) e legenda | [estruturas.md · legenda](references/estruturas.md#legenda) |
| Carrossel | capa, uma ideia por tela, tela final com CTA, legenda | [estruturas.md · carrossel](references/estruturas.md#carrossel) |
| Reels, TikTok, Shorts | gancho dos 3 primeiros segundos, blocos de 3 a 5 s, texto na tela, CTA, legenda | [estruturas.md · roteiro curto](references/estruturas.md#roteiro-curto) |
| Stories | sequência de 3 a 6 telas, uma interação (enquete, caixa, quiz), CTA no fim | [estruturas.md · stories](references/estruturas.md#stories) |
| Vídeo longo | gancho e promessa, partes, resumo, CTA (o método completo está no `video-do-zero`) | [estruturas.md · vídeo longo](references/estruturas.md#vídeo-longo) |
| Perfil | bio, nome de exibição, destaques, link | [estruturas.md · bio](references/estruturas.md#bio) |
| Marca | slogan, frase de posicionamento | [estruturas.md · slogan](references/estruturas.md#slogan) |

## CTA: o verbo pelo objetivo

| Objetivo | CTA que funciona | Evite |
|---|---|---|
| Alcance (o algoritmo distribuir) | "manda pra quem precisa ver", "salva pra fazer depois" | "curte aí" |
| Conversa | uma pergunta fechada e fácil: "qual dos 3 você erra mais?" | "o que vocês acham?" |
| Lista ou lead | "comenta PLANILHA que eu te mando" (palavra-chave curta) | "link na bio" sem dizer o que tem lá |
| Seguir | "segue pra parte 2", com a parte 2 de fato planejada | "segue pra mais conteúdo" |
| Venda | o que a pessoa ganha + onde clicar: "a agenda de novembro abriu, o link está na bio" | urgência falsa, "últimas vagas" sem ser verdade |

O CTA aparece no fim da peça (última tela, últimos segundos) e se repete na legenda. Em vídeo, fala e texto na tela dizem a mesma coisa.

## Onde o texto fica

```
04-marcas/<marca>/<tipo>/<peça>/
├── copy.md        ← ganchos testados, texto das telas, legenda, hashtags, CTA (o scripts/peca.py cria)
├── roteiro.md     ← (vídeo) a fala
└── final/
    └── <tema>-<tipo>-legenda.txt   ← legenda aprovada, pronta para colar
```

Quando o dono aprovar, grave a legenda no arquivo que `uv run scripts/peca.py rascunho <peça> txt --extra legenda` indicar (`rascunhos/<tema>-<tipo>-legenda-v<N>.txt`) e aprove com `uv run scripts/peca.py aprovar <arquivo>`, como qualquer entrega. A capa do Reels e a miniatura do YouTube seguem o mesmo caminho (`--extra capa`, `--extra miniatura`). Gancho que funcionou bem (pelos números da peça) entra no `resultados.md` da marca para ser reaproveitado.

## Revisão antes de entregar

- [ ] O gancho para a rolagem sem o resto da peça? Leia só ele, em voz alta.
- [ ] A peça cumpre a promessa do gancho?
- [ ] Um CTA só, com o verbo do objetivo?
- [ ] Nenhum número, depoimento ou resultado sem fonte?
- [ ] Soa como a marca (`plataforma.md`) e passou pela `humanizer`?
- [ ] Texto da tela legível em 1 segundo por linha (até umas 8 palavras por tela de vídeo, até umas 25 por tela de carrossel)?
- [ ] Legenda: a primeira linha funciona sozinha (é o que aparece antes do "mais")?
- [ ] Ortografia conferida, e nomes de marcas e pessoas escritos certo?

---

Parte dos modelos foi adaptada do pacote `kit-510-ptbr` (pastas 01-conteudo-copy e 09-redes-sociais) do repositório github.com/kursku/skills, © Cafe Code AI, licença MIT. O que foi aproveitado e o que ficou de fora está em [references/origem-kit-510.md](references/origem-kit-510.md).
