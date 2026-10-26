# Synthwave (retrô anos 80)

> Data: 2026-10-25 · Tipo: estilo · Status: vigente

**Resumo:** néon rosa e ciano, pôr do sol em degradê, grade em perspectiva e letreiros cromados. Passa energia noturna, games e nostalgia oitentista.

## Como reconhecer

- Grade em perspectiva até o horizonte, em néon.
- Sol em degradê cortado por faixas horizontais.
- Néon rosa e ciano com brilho (glow).
- Montanhas em wireframe, palmeiras, carros.
- Títulos cromados ou em néon.
- Linhas de varredura (scanlines).

## Paleta

| Papel | Hex |
|---|---|
| Céu noturno | #2B0F54 → #1A1A2E |
| Rosa néon | #FF2A6D |
| Ciano | #05D9E8 |
| Sol | #F9C80E → #FF2A6D |

## Tipografia

Monoton (néon), Orbitron e Audiowide (futuristas). Texto de apoio em sem serifa limpa.

## Forma, composição e textura

- Horizonte no terço inferior, sol atrás do título.
- Brilho em volta das linhas e do texto.
- Scanlines e leve granulação por cima.

## Movimento

- A grade avança em loop contínuo.
- O sol sobe ou pulsa.
- O brilho pulsa na batida.
- Letreiro acende como néon, com pequenas falhas (flicker).
- Transições com faixa de varredura ou chiado de fita.

## Som

Synthwave: baixo arpejado, sintetizadores analógicos, bateria eletrônica com reverb fechado. Marque as batidas com `scripts/som/batida.py`.

## Combina com / evite

| Combina com | Evite quando |
|---|---|
| games, música, eventos noturnos, tecnologia com toque retrô | marcas naturais, orgânicas, saúde, infantil |

## Como fazer no estúdio

- Grade e sol em SVG ou canvas no HyperFrames, com `filter: drop-shadow` para o brilho.
- Blocos prontos de scanline e CRT: skill `hyperframes-registry`.

## Para buscar referências

"synthwave poster", "outrun aesthetic", "retrowave grid", "neon sign animation".

## Armadilhas

- Clichê: use um elemento central forte, não todos os ícones do estilo.
- Brilho demais borra o texto.

## Exemplos salvos
