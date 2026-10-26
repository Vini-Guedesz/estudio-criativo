---
name: redes-sociais
description: Planejamento e estratégia de redes sociais de uma marca do estúdio - o que publicar em cada plataforma (Instagram, Reels, Stories, TikTok, YouTube e Shorts, LinkedIn), calendário editorial e pilares, reaproveitar um conteúdo em vários formatos, hashtags e busca, perfil (bio, destaques), engajamento depois de publicar, auditoria do perfil, leitura de métricas e relatório do mês. Usar quando o pedido for planejar, organizar, analisar ou melhorar a presença da marca nas redes, e não escrever o texto de uma peça (isso é a copy-redes).
---

# Redes sociais: planejar, publicar e aprender

> Data: 2026-10-25 · Tipo: guia · Status: vigente

**Resumo:** como o estúdio decide o que cada marca publica, onde e quando, e como aprende com os números. O plano fica no `calendario.md` da marca e o aprendizado no `resultados.md`. As especificações de cada plataforma estão em [references/plataformas.md](references/plataformas.md), o calendário e o reaproveitamento em [references/calendario.md](references/calendario.md) e as métricas em [references/metricas.md](references/metricas.md).

## Onde cada coisa fica

```
04-marcas/<marca>/
├── calendario.md     ← pilares, ritmo, o plano das próximas semanas e o status de cada peça
├── resultados.md     ← números de cada peça publicada, médias da conta e o que aprendemos
└── <tipo>/<peça>/    ← cada peça do calendário vira uma pasta (scripts/peca.py nova)
```

O calendário diz **o que** e **quando**. A peça diz **como**. Toda linha do calendário que for produzida vira uma pasta com `uv run scripts/peca.py nova <tipo> "tema" --data <dia>`, e a pasta aparece na coluna "Peça".

## Os pedidos e o caminho

| Pedido | O que fazer |
|---|---|
| "Monta o calendário do mês" | [calendario.md](references/calendario.md): pilares → ritmo → ideias → tabela no `calendario.md` da marca. Mostre e ajuste antes de abrir as peças |
| "O que eu posto no TikTok / LinkedIn / YouTube?" | [plataformas.md](references/plataformas.md): formato, duração, o que a plataforma valoriza, adaptação do conteúdo da marca |
| "Transforma esse vídeo em mais conteúdo" | [calendario.md · reaproveitar](references/calendario.md#reaproveitar): uma peça mãe vira cortes, carrossel e stories, cada um como peça nova |
| "Analisa meu perfil" / "o que está dando certo?" | [metricas.md · auditoria](references/metricas.md#auditoria) |
| "Faz o relatório do mês" | [metricas.md · relatório](references/metricas.md#relatório-do-mês) |
| "Por que esse vídeo viralizou?" | analise como referência (`03-referencias/analises/`), com o método de [metricas.md · desmontar](references/metricas.md#desmontar-um-conteúdo-que-funcionou) |
| "Arruma minha bio / meus destaques" | `copy-redes` ([estruturas.md · bio](../copy-redes/references/estruturas.md#bio)) |
| Texto de uma peça (legenda, gancho, carrossel) | skill `copy-redes` |
| Produzir o vídeo | skill `estudio-video` |

## As regras

- **Dado da conta ganha de regra de internet.** Melhor horário, duração ideal e "taxa boa" mudam por público. Use os números das plataformas como ponto de partida e troque pelos da conta assim que houver 10 ou mais peças publicadas no `resultados.md`.
- **Nada de número inventado.** Relatório, auditoria e proposta só citam números que vieram do painel da plataforma ou do dono. Sem acesso ao painel, peça ao dono um print (ele vai para a `00-entrada/`) ou os números, e diga o que ficou sem dado.
- **Cada plataforma é um formato.** O mesmo vídeo pode ir para Reels, TikTok e Shorts, mas a capa, o texto da tela, a legenda e o CTA se ajustam a cada uma. Nunca publique com marca d'água de outra rede.
- **Constância antes de volume.** Um ritmo que o dono consegue manter por meses vale mais que uma semana de 3 posts por dia. O calendário nasce do tempo real de produção.
- **Tendência com critério.** Áudio ou formato em alta só entra quando cabe na voz e num pilar da marca. A fatia sugerida é de no máximo 30% do calendário. O resto é conteúdo que continua útil daqui a um ano.
- **Música licenciada.** Em vídeo que sai do estúdio, a trilha vem da `05-biblioteca/` ou de biblioteca com licença. Áudio em alta da plataforma é colocado no próprio app na hora de publicar, nunca embutido no render.
- **Anúncio é peça.** Post patrocinado, publi e colaboração com outro perfil são marcados como tal (#publi, parceria paga) e registrados no calendário.

## Depois de publicar

1. Nas primeiras horas, responda os comentários (na voz da marca) e fixe o melhor comentário ou um que leve à próxima ação.
2. Repostar nos stories ajuda a peça nova a ser vista por quem já segue.
3. Depois de 7 dias, registre os números da peça no `resultados.md` ([metricas.md](references/metricas.md#o-que-registrar-de-cada-peça)).
4. No fim do mês, o relatório: o que repetir, o que parar, o que testar.

## Revisão do calendário

- [ ] Cada semana tem pelo menos um conteúdo de cada pilar principal?
- [ ] O ritmo cabe no tempo de produção do dono?
- [ ] Cada peça tem objetivo e CTA definidos?
- [ ] Datas da marca e do nicho (lançamentos, feriados que importam ao público) estão no plano?
- [ ] Pelo menos uma peça mãe por mês, com os reaproveitamentos planejados?
- [ ] Linhas produzidas apontam para a pasta da peça?

---

Parte das orientações foi adaptada do pacote `kit-510-ptbr` (pasta 09-redes-sociais) do repositório github.com/kursku/skills, © Cafe Code AI, licença MIT. O que foi aproveitado e o que ficou de fora está em [copy-redes/references/origem-kit-510.md](../copy-redes/references/origem-kit-510.md).
