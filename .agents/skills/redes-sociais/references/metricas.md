# Métricas: registrar, auditar e relatar

> Data: 2026-10-25 · Tipo: guia · Status: vigente

**Resumo:** o que medir em cada peça, como montar a média da própria conta, como auditar um perfil, como desmontar um conteúdo que funcionou e como escrever o relatório do mês. Tudo fica no `resultados.md` da marca. Só entram números do painel da plataforma ou dados que o dono passou.

## Os números que importam

| Métrica | O que diz | Onde ver |
|---|---|---|
| Retenção nos 3 primeiros segundos | se o gancho funcionou | Insights do Reels, TikTok Analytics, YouTube Studio |
| Taxa de conclusão / tempo médio assistido | se o vídeo cumpre a promessa e tem ritmo | idem |
| Envios (compartilhamentos) | se a peça vale ser mostrada a alguém. É o sinal mais forte de alcance | idem |
| Salvamentos | se a peça é útil para depois | Instagram |
| Comentários | se a peça abre conversa | todas |
| Alcance de não seguidores | se a peça saiu da bolha | Instagram, TikTok |
| Seguidores ganhos pela peça | se a peça convence a seguir | Instagram, TikTok |
| Cliques no link / visitas ao perfil | se o CTA de venda funcionou | Instagram, TikTok |
| CTR da miniatura | se o título e a capa fazem clicar | YouTube Studio |

Curtida é o número menos útil. Não decida nada por ela.

## O que registrar de cada peça

Sete dias depois de publicar, uma linha no `resultados.md` da marca:

| Data | Peça | Plataforma | Formato | Pilar | Gancho (tipo) | Alcance | Ret. 3 s | Conclusão | Envios | Salvos | Coment. | Seguidores | Nota |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

Com 10 peças ou mais registradas, calcule a **média da conta** por formato e escreva no topo do arquivo. A partir daí, uma peça "foi bem" quando passa da média da própria conta, não de um número da internet.

## Auditoria

Para "analisa meu perfil" ou antes de começar a cuidar de uma marca existente:

1. **Perfil:** nome de exibição, bio, link, destaques, foto. Está claro em 3 segundos o que a marca faz e para quem? (modelo de bio na `copy-redes`)
2. **Grade:** os últimos 9 a 12 posts são coerentes com a identidade? Dá para reconhecer a marca sem ver o nome?
3. **Conteúdo dos últimos 90 dias:** liste as peças por formato e pilar. Quais pilares sumiram? Qual formato domina?
4. **Números:** com os dados do painel (ou prints que o dono mandar para a `00-entrada/`), separe as 5 melhores e as 5 piores peças pelo critério do objetivo (envios e salvamentos para alcance, cliques para venda).
5. **Comparação:** de 3 a 5 perfis parecidos (concorrentes ou referências). O que eles fazem com regularidade que a marca não faz?
6. **Entrega:** o que está bom (manter), as 3 maiores oportunidades (com o porquê) e as 3 primeiras ações. Salve como `04-marcas/<marca>/auditoria-AAAA-MM-DD.md`.

## Desmontar um conteúdo que funcionou

Para entender por que um vídeo ou post foi bem (da marca ou de referência):

1. **Gancho:** o que se vê, se lê e se ouve nos 3 primeiros segundos. De qual tipo é ([ganchos.md](../../copy-redes/references/ganchos.md))?
2. **Estrutura:** a sequência (gancho, problema, solução, CTA ou outra). Quanto tempo dura cada bloco?
3. **Ritmo:** a cada quantos segundos algo muda na tela?
4. **Promessa e entrega:** o que o gancho promete e quando entrega?
5. **Por que alguém mandaria isso para outra pessoa?** Essa resposta costuma ser o motivo do alcance.
6. **O que dá para levar para a marca** (estrutura, tipo de gancho, ritmo), e o que não combina com a voz dela.

Referência externa vira análise em `03-referencias/analises/AAAA-MM-DD-assunto.md` (padrão do `03-referencias/_LEIA.md`). Para vídeo, use a skill `watch` e o `scripts/video/olho_quadro_a_quadro.py`.

## Relatório do mês

Salve em `04-marcas/<marca>/resultados.md`, numa seção nova no topo (`## Novembro de 2026`):

1. **Resumo em 3 linhas:** como foi o mês comparado à média da conta.
2. **Os números do mês:** peças publicadas por formato e pilar, seguidores ganhos, alcance total, as médias de retenção, envios e salvamentos.
3. **As 3 melhores e as 3 piores**, com o porquê provável de cada uma (gancho, tema, formato, horário).
4. **O que aprendemos:** o que repetir, o que parar, o que testar no mês que vem. Cada teste tem uma hipótese ("gancho de erro comum retém mais que lista").
5. **Ajustes no calendário** do próximo mês.

Aprendizado que vale para qualquer marca (técnica de vídeo, ritmo, edição) também vai para `06-metodo/aprendizados.md`.
