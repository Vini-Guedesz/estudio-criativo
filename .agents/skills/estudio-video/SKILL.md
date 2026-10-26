---
name: estudio-video
description: Ponto de entrada de qualquer pedido de vídeo neste estúdio (Reel, anúncio, tutorial narrado, vídeo de produto, motion, edição de bruto, legenda). Usar no começo de todo vídeo para abrir o método, escolher o motor (After Effects, EffectCraft, HyperFrames ou Remotion) e a skill de receita certa, sempre com referências antes de animar.
---

# Estúdio de vídeo: por onde começar

> Data: 2026-10-22 · Tipo: guia · Status: vigente

**Resumo:** roteador de vídeo. Diz em que ordem trabalhar, qual motor usar e qual skill seguir para cada tipo de peça. O método completo está em [video-do-zero](../../../06-metodo/video-do-zero.md); os números (mola, câmera, volume, render) moram só em [regras.md](../../../06-metodo/regras.md).

## Antes de animar qualquer coisa

1. **Combine o "pronto"** (formato, duração, onde vai ser publicado) e abra a peça com `uv run scripts/peca.py nova <reels|videos|stories> "tema"` (cria `04-marcas/<marca>/<tipo>/AAAA-MM-DD-tema/`, padrão em `04-marcas/_LEIA.md`), com o checklist do [video-do-zero](../../../06-metodo/video-do-zero.md) no `README.md`.
2. **Áudio aprovado primeiro.** Narração, se houver, é aprovada pelo dono antes da edição: todo o resto é sincronizado com ela.
3. **Referências antes de produzir:** siga a skill [video-referencias](../video-referencias/SKILL.md). Procure antes em `03-referencias/` ([como funciona](../../../03-referencias/_LEIA.md)) e na `05-biblioteca/`.
4. **Identidade do vídeo** tirada do assunto, e **direção** decidida antes de animar: [references/identidade.md](references/identidade.md) e [references/direcao.md](references/direcao.md).
5. **Briefing e storyboard aprovados** (seção abaixo).

## Escolher o motor

A tabela geral de qual ferramenta usar (inclusive foto e logo) está em [02-ferramentas/_LEIA.md](../../../02-ferramentas/_LEIA.md#qual-ferramenta-usar). Na dúvida entre dois motores, faça os mesmos 3 segundos nos dois e compare lado a lado. Confira o que está instalado em `02-ferramentas/` ([modelo dos docs](../../../02-ferramentas/_LEIA.md)) antes de decidir.

| Motor | Quando | Como o agente usa |
|---|---|---|
| **After Effects** | acabamento fino: molas, câmera 3D, transições, efeitos | ExtendScript e expressões (o AE é opcional e pago; sem ele, use o EffectCraft) |
| **EffectCraft** | alternativa gratuita e aberta ao After Effects | servidor MCP `effectcraft`: `command_list` para achar o comando, `command_run` para executar, `render_preview` para olhar |
| **HyperFrames** | vídeo em HTML/GSAP: telas, texto animado, peças em série | `npx skills add heygen-com/hyperframes`; comece pela skill `hyperframes` |
| **Remotion** | vídeo em React, componentes reutilizáveis | `npx skills add remotion-dev/skills`; skill `remotion-best-practices` |

Partes podem nascer em código (HyperFrames ou Remotion) e ser finalizadas no After Effects ou no EffectCraft. Em qualquer motor, **olhe o quadro renderizado** antes de dizer que está pronto: resultado de ferramenta não é prova.

## Escolher a receita

| Pedido | Skill |
|---|---|
| Peça ou marca sem direção visual, links de referência, "quero nesse estilo" | [referencias-e-estilos](../referencias-e-estilos/SKILL.md) (mural, fichas de estilo, direções) |
| Qualquer vídeo com motion | [video-referencias](../video-referencias/SKILL.md) antes de tudo |
| Narrado: explicativo, tutorial, anúncio com voz | [motion-narrado](../motion-narrado/SKILL.md) |
| Produto, software, lançamento, "apresentando", demo | [animacao-saas](../animacao-saas/SKILL.md) (narrado: soma com a `motion-narrado`) |
| Tela de app ou site recriada dentro do vídeo | [ui-para-video](../ui-para-video/SKILL.md) |
| Trilha, efeitos, mix | [som-do-video](../som-do-video/SKILL.md) |
| Assistir a um vídeo (referência, concorrente) | skill `watch` |
| Bruto com fala | `uv run scripts/video/cut_pauses.py` corta pausas; `uv run scripts/video/make_captions.py` gera a legenda |
| Gancho, texto na tela, legenda do post, CTA | [copy-redes](../copy-redes/SKILL.md) |
| Onde e quando publicar, cortes de um vídeo longo, números depois de publicar | [redes-sociais](../redes-sociais/SKILL.md) |

## Briefing e storyboard antes de animar

O briefing vai no `README.md` do projeto, sempre nestas seções:

1. objetivo e entrega (formato, quadros por segundo, duração, projeto editável);
2. linguagem visual (cores em hex, fonte, regras de composição);
3. assets e de onde vem cada um;
4. sequência com o tempo de cada cena;
5. regras de movimento;
6. som como relógio (batidas, drop, fala);
7. como o render será conferido.

O storyboard (quadros estáticos ou tabela cena → tempo → o que entra) é aprovado **antes** de animar. Antes de inventar uma saída de cena, veja o catálogo aberto em [references/saidas-e-truques.md](references/saidas-e-truques.md).

## Ver rápido, entregar uma vez

- **Prévia a cada ajuste** (meia resolução, sem desfoque de movimento) para conferir montagem, tempo e som. Prévia nunca é entregue.
- **Final uma vez.** Depois de um ajuste, refaça só o trecho que mudou.
- **Som em paralelo:** com a primeira prévia pronta, o som pode andar sozinho pelos eventos da animação (`uv run scripts/som/som.py --eventos eventos.json ...`). Detalhes na `som-do-video`.

## Revisar

1. `uv run scripts/video/detectar_saltos.py rascunhos/<tema>-<tipo>-v<N>.mp4` (todo render sai em `rascunhos/` da peça, com o nome de `scripts/peca.py rascunho`; o aprovado vai para `final/` com `scripts/peca.py aprovar`): todo salto restante tem de ser corte de propósito.
2. `uv run scripts/video/olho_quadro_a_quadro.py compara` contra a referência: curvas do original e da recriação no mesmo gráfico.
3. Original em cima, nosso embaixo, no tamanho do celular. A pergunta: **"o original grita mais?"** (contraste, tamanho, peso do texto). Se sim, ainda não superou.
4. Registre no `README.md` do projeto e numa anotação. Número que funcionou vai para [regras.md](../../../06-metodo/regras.md).
