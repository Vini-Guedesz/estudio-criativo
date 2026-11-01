# Origem da skill canal-dark

> Data: 2026-11-01 · Tipo: dados · Status: vigente

**Resumo:** de onde veio cada parte da skill, o que foi aproveitado, o que mudou e o que ficou de fora de propósito. Todo o material de terceiros é MIT; os créditos e o texto da licença estão em [TERCEIROS.md](../../../../TERCEIROS.md). Nada foi copiado inteiro: as ideias foram reescritas em português, cortadas para o estúdio e ligadas às skills que já existem. O levantamento completo está em [03-referencias/analises/2026-11-01-skills-canal-dark.md](../../../../03-referencias/analises/2026-11-01-skills-canal-dark.md).

## O que veio de onde

| Repositório | Aproveitado | Onde está |
|---|---|---|
| [kamalammouri/faceless-video-skills](https://github.com/kamalammouri/faceless-video-skills) | normas fixas do canal e por quê; teste do espelho; estrutura do explicador em 8 tempos; folha de ritmo da história de sobrevivência; ritmo cena-insert-cena; inserts por código para números; palavras proibidas no prompt; regras da miniatura; ficha de publicação; Short de chamada com o comando ffmpeg; auditoria de um gargalo por vez; lista do que nunca recomendar | formatos.md, roteiro.md, visual.md, publicacao.md, crescimento.md, normas-do-canal.md |
| [DamaizLabs/lanternist](https://github.com/DamaizLabs/lanternist) | paradas de aprovação do dono ("conversar não é aprovar", palavras literais e data); decisões anotadas; fontes lidas e não lidas e as formas sutis de afirmar; números com ano e lugar; revisão em duas etapas (revisor e refutador); "nomear desenha"; escrever para a voz (pontuação, onomatopeia, sussurro); trocar o texto e manter a semente; só a voz do dono ou de catálogo; o estúdio não publica | SKILL.md, roteiro.md, visual.md |
| [kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director) | arco em 5 etapas; âncora do personagem repetida igual; personagem sempre em ação concreta; sem texto e sem código de cor no prompt; kit de publicação em 5 itens; capítulos só com os tempos reais | formatos.md, roteiro.md, visual.md, publicacao.md |
| [AgriciDaniel/claude-youtube](https://github.com/AgriciDaniel/claude-youtube) | sistemas separados de distribuição; teste em ondas; sinais de satisfação; "algoritmo é o público"; estrutura dos primeiros 30 s; chamada no meio; diagnóstico pela curva de retenção; miniatura (palavras, espaço vazio, celular, não repetir o título); descrição, capítulos, hashtags e tags; vídeos fora da curva; regra dos 100 vídeos | roteiro.md, visual.md, publicacao.md, crescimento.md, regras.md |
| [AgriciDaniel/claude-shorts](https://github.com/AgriciDaniel/claude-shorts) | nota dos trechos para cortes (5 critérios com peso); ajustar o corte às pausas | crescimento.md |
| [hassancs91/claude-faceless-shorts-creator](https://github.com/hassancs91/claude-faceless-shorts-creator) | gramática do Short próprio: quadro 0 já montado, revelação em passos, loop no último quadro, sem "comenta aí" no fim; folga de palavras por segundo na narração | formatos.md, regras.md |
| [sergebulaev/youtube-skills](https://github.com/sergebulaev/youtube-skills) | título e miniatura como par; nunca inventar número para parecer real; abrir sem saudação | roteiro.md, visual.md, publicacao.md |

A biblioteca [zhuyansen/awesome-claude-video-skills](https://github.com/zhuyansen/awesome-claude-video-skills) (lista CC0) serviu para achar os três últimos. Também apontou o [explainroo](https://github.com/vincentsch/explainroo) e a voz Kokoro, que fala português do Brasil e roda no computador, registrada como opção em [02-ferramentas/voz.md](../../../../02-ferramentas/voz.md).

## O que ficou de fora, e por quê

- **Números de mercado sem fonte verificável** (por exemplo "narração de IA tem 70% menos retenção", "+921 mil views com rosto na miniatura", taxas de clique por nicho). Vieram de blogs e agências e não dava para conferir. O estúdio não repete número que não sabe de onde veio.
- **Automação do Google Flow pelo Chrome** (faceless-video-skills): controla uma interface sem API, depende de plano pago e pode ferir os termos do Google.
- **Motores próprios** (Lanternist com ComfyUI, Orpheus e 95 GB; os renderizadores do stickman e do shorts-creator): o estúdio já tem HyperFrames, Remotion e EffectCraft. Os métodos vieram; os motores, não.
- **Upload automático e agendamento em massa** (Publora, faceless.so, os repositórios de "piloto automático"): o estúdio não publica sem o dono.
- **Regras de canais específicos** (mascote "caveman", horário do Marrocos, molde "Why Evolution"): viraram campos do modelo de normas, para cada canal decidir os seus.
- **Imitar canais nomeados** e "colar o link de um canal e ganhar um canal igual" (shadowcast e parecidos): é o que a política de conteúdo inautêntico pune.
- **DataForSEO, NanoBanana e outras integrações pagas** do claude-youtube: opcionais e pagas; dá para instalar a skill original se o dono quiser.
