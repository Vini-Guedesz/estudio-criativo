# Skills de canal dark (faceless) e regras de conteúdo com IA

> Data: 2026-11-01 · Tipo: análise · Status: vigente

**Resumo:** levantamento de skills públicas (GitHub) para produzir, manter e crescer um canal dark no YouTube, mais o que as plataformas fazem hoje com conteúdo feito por IA. O que serviu foi adaptado para a skill `canal-dark` (ver o fim deste doc). A conclusão principal: o que derruba canal dark não é a IA ser detectada, e sim vídeo genérico e repetido (política de "conteúdo inautêntico" do YouTube).

## O que as plataformas fazem (out/2026)

- **YouTube:** desde julho de 2025 a regra de "conteúdo repetitivo" virou **"conteúdo inautêntico"**. Em 13/07/2026 o YouTube detalhou três tipos que perdem monetização: (1) conteúdo genérico, em série, que parece saído de um molde; (2) conteúdo insatisfatório ou manipulador; (3) "especialistas" falsos feitos por IA, principalmente em saúde, finanças, direito e política. Segundo as fontes, a regra não olha a ferramenta, olha o vídeo pronto. Canal sem rosto continua elegível se cada vídeo tiver narrativa, opinião ou pesquisa que um molde não produziria. Conteúdo realista alterado ou sintético precisa ser marcado no Studio ("conteúdo alterado ou sintético"). Fonte principal: [Tubefilter](https://www.tubefilter.com/2026/07/13/youtube-inauthentic-content-monetization-policy-update/). O "sistema de três avisos" citado por blogs não foi confirmado em documento oficial.
- **TikTok:** rotula IA sozinho lendo metadados C2PA (e, segundo blogs de 2026, marca d'água invisível e classificadores). O rótulo automático não sai. O criador também é obrigado a rotular conteúdo realista.
- **Instagram/Facebook (Meta):** rotula quando encontra sinais C2PA/IPTC de IA no arquivo.
- **Implicação para o estúdio:** tentar esconder a IA (tirar metadados, burlar detector) viola as regras das plataformas e não resolve o problema real. O que protege as views é originalidade: roteiro com pesquisa e ponto de vista, visual próprio (o estúdio já tem HyperFrames, Remotion, EffectCraft), variedade entre vídeos, rótulo quando exigido e um humano aprovando antes de publicar.

## Skills encontradas

### Recomendadas para avaliar primeiro

| Repo | O que faz | Licença / sinais | Observações |
|---|---|---|---|
| [AgriciDaniel/claude-youtube](https://github.com/AgriciDaniel/claude-youtube) | Uma skill com 14 comandos: auditoria de canal, SEO, roteiro com retenção, gancho, thumbnail, estratégia, calendário, Shorts, análise, monetização, concorrentes, ideias | MIT, ~625 estrelas, beta, inglês | Só aconselha, não publica. Sem chave paga obrigatória (YouTube Data API é grátis). Cobre bem o "como manter" |
| [kaomei/stickman-video-director](https://github.com/kaomei/stickman-video-director) | Direção de vídeos de bonequinho (stickman) faceless | MIT, ~3,6 mil estrelas, ativo (out/2026) | Precisa de chaves de terceiros (Gemini, Claude ou ElevenLabs). FAQ cita a política de conteúdo reusado do YouTube |
| [DamaizLabs/lanternist](https://github.com/DamaizLabs/lanternist) | 6 skills: instalar, propor formato, criar canal, produzir a semana, roteiro para slides, encenar | MIT, 15 estrelas, ativo, espanhol | Melhor prática de transparência: C2PA + marca d'água em tudo, não publica sozinho. Pesado: Windows 11, GPU NVIDIA 8 GB+, 32 GB RAM, ~95 GB |
| [kamalammouri/faceless-video-skills](https://github.com/kamalammouri/faceless-video-skills) | Roteiros de explicador científico, história de sobrevivência, "E se você...", e visuais desenhados em código | MIT, 0 estrelas, instruções em francês | Bom como modelo de formato. Imagens dependem de automatizar o Google Flow pelo Chrome (conta AI Pro/Ultra; checar termos do Google). Copia regras de canais específicos |
| [sergebulaev/youtube-skills](https://github.com/sergebulaev/youtube-skills) | 9 skills: título, descrição, gancho, thumbnail, post da comunidade, plano, reaproveitamento, otimização de canal, leitura de comentários | MIT, 81 estrelas | Aprova antes de publicar. **Atenção:** o texto fala em "tirar as marcas de IA" e "pegar o rascunho arriscado antes da plataforma"; ler `references/voice-rules.md` antes de usar |
| [adityaarsharma/youtube-marketing-skills](https://github.com/adityaarsharma/youtube-marketing-skills) | 21 comandos + servidor MCP com dados ao vivo do canal | MIT, 76 estrelas | Precisa de projeto no Google Cloud e OAuth. O SEO em lote altera vários vídeos de uma vez |

### Úteis como peça, não como pipeline

- [apenasdouglas/ai-motion-library](https://github.com/apenasdouglas/ai-motion-library): biblioteca de efeitos de motion para documentário, em português. MIT, 75 estrelas.
- [iliasabk/claude-skill-media-pipeline](https://github.com/iliasabk/claude-skill-media-pipeline): imagens, voz, ffmpeg, Shorts e upload. Precisa de chave fal.ai (~US$0,75 por vídeo de 6 min). Sobe para o YouTube sem passo de aprovação, e os comandos de instalação citam três donos diferentes: conferir antes.
- [TheNoumanDev/zero-dollar-studio](https://github.com/TheNoumanDev/zero-dollar-studio): só macOS, não serve neste PC.

### Evitar

- [Side-Products/faceless-skill](https://github.com/Side-Products/faceless-skill): sem licença, depende do SaaS pago Faceless.so e posta em sete redes.
- generalizingai/shadowcast e os repos de "piloto automático" com upload sem revisão (raunakpatil/youtube-agentic-ai-studio, metiutek/tube-assistant, money-printer-pro etc.): clonar o formato de outro canal e publicar em massa é exatamente o que a política de conteúdo inautêntico pune.

## O que já existe no estúdio e cobre parte disso

Skills `estudio-video`, `motion-narrado`, `som-do-video`, `video-referencias`, `copy-redes`, `redes-sociais`, `humanizer`, `media-use`, `watch`, HyperFrames e Remotion. Falta: estratégia e SEO específicos de YouTube, roteiro longo com retenção e um checklist de originalidade e rótulo de IA.

## Outras fontes

- [Tópico faceless-youtube no GitHub](https://github.com/topics/faceless-youtube) (59 repos; vistos os 20 primeiros)
- [Tubefilter sobre o rótulo automático do TikTok](https://www.tubefilter.com/?p=180011)
- [Billo: rótulos de IA em 2026](https://billo.app/blog/ai-labeling/)

## Segunda rodada: leitura completa (01/11/2026)

Os repositórios foram clonados e lidos por inteiro, junto com a biblioteca [zhuyansen/awesome-claude-video-skills](https://github.com/zhuyansen/awesome-claude-video-skills) (394 repositórios de vídeo, lista CC0). Da biblioteca, três entraram na leitura: [claude-faceless-shorts-creator](https://github.com/hassancs91/claude-faceless-shorts-creator), [claude-shorts](https://github.com/AgriciDaniel/claude-shorts) e [explainroo](https://github.com/vincentsch/explainroo) (voz local Kokoro, que fala português do Brasil).

As regras do YouTube foram conferidas nas páginas oficiais. Correção em relação à primeira rodada: o "sistema de três avisos" dos blogs não aparece na página oficial. O que a página diz é que quem deixa de rotular com frequência pode receber o rótulo à força, ter vídeo removido ou ser suspenso do Programa de Parceria, e que **rotular não reduz alcance nem monetização**. Resumo completo em `.agents/skills/canal-dark/references/politicas-ia.md`.

**Resultado:** nova skill `.agents/skills/canal-dark/`. O que veio de cada repositório e o que ficou de fora (números sem fonte, automação do Google Flow, motores próprios, upload automático, imitação de canais) está em `.agents/skills/canal-dark/references/origem.md`. Os números de partida foram para `06-metodo/regras.md` (seção Canal dark). Os créditos MIT estão em `TERCEIROS.md`.
