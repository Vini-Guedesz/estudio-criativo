# Pixel art

> Data: 2026-10-25 · Tipo: estilo · Status: vigente

**Resumo:** imagem montada pixel a pixel numa grade visível, com paleta curta, como nos jogos de 8 e 16 bits. Passa nostalgia, humor e cultura gamer.

## Como reconhecer

- Grade de pixels visível e de tamanho único na cena inteira.
- Nenhum anti-aliasing: bordas em degrau, sem meio-tom suave.
- Paleta limitada (de 4 a 32 cores).
- Sombra e volume feitos com pontilhado (dithering, o padrão xadrez) e não com degradê.
- Contorno de 1 pixel, escuro ou colorido.
- Elementos de jogo: sprites, caixas de diálogo, barra de vida, moedas, placar.

## Paleta

| Paleta | Cores |
|---|---|
| PICO-8 (16 cores, versátil) | #000000 #1D2B53 #7E2553 #008751 #AB5236 #5F574F #C2C3C7 #FFF1E8 #FF004D #FFA300 #FFEC27 #00E436 #29ADFF #83769C #FF77A8 #FFCCAA |
| Game Boy (4 verdes) | #0F380F #306230 #8BAC0F #9BBC0F |

Para uma marca, reduza a paleta dela a 8 ou 16 cores e acrescente 1 ou 2 tons de sombra para cada cor principal.

## Tipografia

Press Start 2P (títulos, bem pequena e quadrada), VT323 (texto, cara de terminal), Silkscreen e Pixelify Sans. Use sempre em tamanho múltiplo exato da grade (8, 16, 24, 32 px...), senão os pixels da letra deformam.

## Forma, composição e textura

- Trabalhe numa resolução baixa e amplie por um número inteiro. No vertical, 180x320 ampliado 6 vezes dá 1080x1920.
- Ampliação sempre com vizinho mais próximo (nearest neighbor), nunca bilinear.
- Composição de tela de jogo: chão, personagem, interface nas bordas.
- Sem rotação livre e sem escala quebrada: isso cria pixels de tamanhos diferentes.

## Movimento

- Animação em poucos quadros (de 2 a 8 por ciclo), trocando a 8 a 12 quadros por segundo, mesmo com o vídeo a 30 ou 60. Isso difere do ritmo do `regras.md` de propósito: anote no projeto.
- Movimento em passos de pixel inteiro, sem deslize suave e sem motion blur.
- Quique e queda de jogo: subida rápida, pausa curta no alto, queda.
- Transições: pixelizar (mosaico crescendo e diminuindo), cortina em blocos, fade em degraus de paleta, tela de "fase concluída".

## Som

Chiptune (música de console antigo) e efeitos 8 bits: moeda, pulo, "blip" de texto aparecendo letra a letra. O sfxr (sfxr.me) gera efeitos assim no navegador. Nivele os efeitos com `scripts/som/nivelar.py`.

## Combina com / evite

| Combina com | Evite quando |
|---|---|
| games, apps, tecnologia, humor, nostalgia, educação gamificada, marcas jovens | luxo, saúde séria, finanças conservadoras, público que não reconhece a referência de jogo |

## Como fazer no estúdio

- **Sprites e cenários:** Aseprite (pago) ou Piskel e LibreSprite (gratuitos). Exporte PNG na resolução baixa.
- **HyperFrames/Remotion:** `image-rendering: pixelated` nas imagens e no canvas; animação com `steps(n)` em vez de easing; posições arredondadas para a grade.
- **Ampliar vídeo pronto:** `ffmpeg -i baixo.mp4 -vf scale=1080:1920:flags=neighbor alto.mp4`.
- **IA de imagem:** "pixel art, 16-bit, limited palette, no anti-aliasing, clean outlines". O resultado quase sempre sai com pixels irregulares. Reduza para a grade com vizinho mais próximo, force a paleta e retoque à mão.

## Para buscar referências

"pixel art animation loop", "16-bit UI", "pixel art scene", "dithering", "sprite sheet". Exemplos conhecidos para estudar: eBoy, Celeste, Stardew Valley, Hyper Light Drifter.

## Armadilhas

- Pixels de tamanhos diferentes na mesma cena (o erro mais comum).
- Degradê suave ou sombra desfocada por cima do pixel art.
- Fonte pixel em tamanho que não é múltiplo da grade.
- Texto longo em fonte pixel: cansa. Use para títulos e rótulos.

## Exemplos salvos
