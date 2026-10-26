# VHS e lo-fi analógico

> Data: 2026-10-25 · Tipo: estilo · Status: vigente

**Resumo:** cara de fita de vídeo e câmera caseira dos anos 90: ruído, cores lavadas, aberração cromática e marcação "REC". Passa intimidade, bastidor e nostalgia.

## Como reconhecer

- Ruído e granulação, cores lavadas e pretos acinzentados.
- Aberração cromática (bordas magenta e verde).
- Linhas de tracking e saltos de imagem.
- Texto de câmera: "REC", data e hora, "PLAY ▶".
- Leve desfoque, às vezes quadro 4:3 dentro do vertical.

## Paleta

Dessaturada, com pretos levantados. Magenta e verde só nas bordas da aberração. Texto de interface em branco ou ciano.

## Tipografia

VT323, IBM Plex Mono ou Space Mono para os textos de câmera. Legendas em sem serifa simples.

## Forma, composição e textura

- Imagem real (gravação) como base.
- Moldura 4:3 ou cantos escurecidos.
- Ruído e scanlines por cima de tudo, em intensidade baixa.

## Movimento

- Câmera na mão, com tremida.
- Salto de tracking nas trocas de cena.
- Rebobinar (imagem acelerando para trás com faixas).
- Congelamento com barra de pausa, cortes secos.

## Som

Chiado de fita, zumbido, botão de câmera, lo-fi hip hop.

## Combina com / evite

| Combina com | Evite quando |
|---|---|
| bastidor, moda streetwear, música, marca pessoal, nostalgia | demonstração de produto ou interface que precisa ser nítida |

## Como fazer no estúdio

- **ffmpeg:** `noise`, `rgbashift` (aberração), `eq=saturation=0.7`, `curves` para levantar os pretos.
- **Looks prontos:** skills `media-use` (cor e aparência) e `hyperframes-registry` (VHS, film grain).
- **After Effects/EffectCraft:** Noise, deslocamento de canal, Wave Warp leve.

## Para buscar referências

"VHS aesthetic", "camcorder footage", "lo-fi video edit", "VHS glitch transition".

## Armadilhas

- Efeito tão forte que o conteúdo some.
- Texto pequeno com ruído: ilegível.

## Exemplos salvos
