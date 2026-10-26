# Kit 510 (kursku/skills): pacotes de copy e redes sociais

> Data: 2026-10-25 · Tipo: fonte · Status: vigente

**Resumo:** análise das pastas `01-conteudo-copy` (32 skills) e `09-redes-sociais` (33 skills) do pacote `kit-510-ptbr` do repositório github.com/kursku/skills (Cafe Code AI, licença MIT declarada em cada skill). O que serviu para um estúdio de vídeo e posts virou as skills `copy-redes` e `redes-sociais`. O resto foi descartado pelos motivos abaixo.

- **Origem:** https://github.com/kursku/skills/tree/master/packs/kit-510-ptbr/01-conteudo-copy e .../09-redes-sociais (lido em 2026-10-25, commit mais recente do branch `master`)
- **Licença:** MIT no cabeçalho de cada `SKILL.md` (autor Cafe Code AI). O repositório não tem arquivo LICENSE na raiz. O crédito está no rodapé das duas skills.

## Como o pacote é

- Cada skill segue o mesmo molde: Keywords, Quick Start, 2 workflows, templates, checklist, "métricas de referência", erros comuns, dicas avançadas.
- **Pontos fortes:** as estruturas clássicas bem explicadas (gancho → problema → solução → CTA, PAS, AIDA, SCQA, jornada do herói), a ideia de pensar o vídeo para ser visto sem som, blocos visuais de 3 a 5 segundos, regra 70/30 entre conteúdo perene e tendência, reaproveitamento de uma peça mãe em vários formatos, "somos / não somos" para a voz da marca, tom que muda por situação, um CTA por peça.
- **Pontos fracos:**
  - Exemplos de vendedor de infoproduto ("dobre suas vendas em 30 dias", "últimas vagas", caixa alta e emoji em excesso). Isso vai contra a voz que o estúdio quer e contra a skill `humanizer`.
  - Estatísticas sem fonte nos exemplos ("70% dos recrutadores", "92% dos usuários", "mais de 10.000 atletas") e tabelas de "benchmark" sem origem (CTR, taxa de engajamento, melhores horários). Não servem como referência.
  - Horários "ideais" fixos por plataforma, que dependem do público de cada conta.
  - Vários arquivos terminam cortados no meio da frase (por exemplo, `hooks-swipe-file` para em "Template de Hook de Des", `carousel-creator` para no slide 6).
  - Descrições genéricas no cabeçalho ("Skill especializada em conteúdo & copywriting"), que não ajudam o agente a saber quando usar.
  - Muita sobreposição: o mesmo roteiro "gancho, problema, solução, CTA" aparece em uns 10 arquivos.

## O que entrou no estúdio

| Skill de origem | Onde foi parar |
|---|---|
| hooks-swipe-file, headline-formulas, viral-content-formula (ganchos) | `copy-redes/references/ganchos.md`: banco de tipos de gancho, regras das 3 camadas (ver, ler, ouvir), o que evitar |
| storytelling-framework, video-script, cta-optimizer | `copy-redes/references/estruturas.md` (estruturas de base) e `copy-redes/SKILL.md` (tabela de CTA por objetivo) |
| instagram-caption, carousel-creator, stories-strategy, reels-content-plan, short-form-video-plan | `copy-redes/references/estruturas.md`: legenda, carrossel tela a tela, roteiro curto em blocos, stories |
| bio-writer, tagline-generator | `copy-redes/references/estruturas.md`: bio, destaques, slogan |
| brand-voice-guide, rewrite-improver | `copy-redes/references/voz-da-marca.md` e o passo 3 do `setup/4-marca.md` |
| instagram-strategy, tiktok-strategy, youtube-strategy, linkedin-strategy, short-form-video-plan, hashtag-strategy | `redes-sociais/references/plataformas.md` |
| content-calendar, social-media-calendar, content-repurposing | `redes-sociais/references/calendario.md` e o modelo `04-marcas/_modelo-marca/calendario.md` |
| social-media-audit, social-media-report, engagement-tactics, viral-content-formula (desmontar o viral) | `redes-sociais/references/metricas.md`, `redes-sociais/SKILL.md` (depois de publicar) e o modelo `resultados.md` |

**Adaptações feitas:** texto reescrito em português simples e no formato do estúdio; exemplos de vendedor trocados por exemplos neutros (confeitaria, estúdio de pilates); todas as estatísticas e benchmarks retirados e trocados pela regra "compare com a média da própria conta"; horários fixos trocados por "use o painel da conta"; números de formato centralizados em `06-metodo/regras.md` (seção Redes sociais); tudo ligado à estrutura `04-marcas/` (`copy.md` em cada peça, `calendario.md` e `resultados.md` em cada marca).

## O que ficou de fora e por quê

- **Fora do escopo de vídeo e post:** blog-seo-writer, seo-meta-writer, email-subject-lines, newsletter-writer, press-release, sales-page-copy, script-cold-outreach, webinar-script, whatsapp-scripts, whatsapp-community, podcast-outline, faq-generator, micro-copy (texto de interface), product-description, case-study-writer, comparison-content, review-response.
- **Gestão e operação, não produção:** community-management, crisis-management-social, social-listening, employee-advocacy, dark-social-strategy, influencer-outreach, social-commerce, social-ads-organic-sync, creator-economy-guide, live-streaming-guide.
- **Plataformas fora do foco atual:** pinterest-strategy, twitter-x-strategy, thread-twitter-x. Se a marca usar, vale reler e acrescentar uma seção em `plataformas.md`.
- **Conteúdo datado:** algorithm-update-tracker (regras de algoritmo envelhecem em meses).
- **Ficaram para depois, se surgir a necessidade:** ad-copy-variants (variações de anúncio pago), ugc-brief (briefing para criador de UGC), collab-post-strategy, user-generated-content, social-proof-collection, meme-marketing. Têm partes úteis, mas o estúdio ainda não faz esse tipo de peça.

## Para reler a fonte

`git clone --depth 1 --filter=blob:none --sparse https://github.com/kursku/skills.git` e `git sparse-checkout set packs/kit-510-ptbr/01-conteudo-copy packs/kit-510-ptbr/09-redes-sociais`.
