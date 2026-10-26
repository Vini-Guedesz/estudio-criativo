# Glassmorfismo

> Data: 2026-10-25 · Tipo: estilo · Status: vigente

**Resumo:** painéis como vidro fosco sobre um fundo colorido e desfocado, com borda fina clara e profundidade em camadas. Passa tecnologia, leveza e acabamento digital.

## Como reconhecer

- Painel translúcido que desfoca o que está atrás.
- Borda fina clara e semitransparente, que simula a quina do vidro.
- Fundo vivo: degradê ou manchas de cor desfocadas (sem fundo colorido, o vidro some).
- Cantos bem arredondados.
- Sombra suave e ampla, ícones de traço fino.

## Paleta

| Papel | Valor |
|---|---|
| Fundo | degradê vivo: #6A5AE0 → #FF6FD8 ou #00C6FB → #005BEA |
| Vidro | branco com 10% a 25% de opacidade |
| Borda | branco com 30% a 40% de opacidade |
| Texto | branco (fundo escuro) ou #1A1A2E (fundo claro), com contraste conferido |

## Tipografia

Inter, Manrope ou Plus Jakarta Sans. Pesos médios, tamanhos generosos, pouco texto por painel.

## Forma, composição e textura

- Duas a três camadas de profundidade: fundo, painéis, conteúdo.
- Manchas de cor atrás dos painéis, nunca atrás do texto principal.
- Brilho sutil no canto superior do painel (reflexo).

## Movimento

- Paralaxe: camadas se movem em velocidades diferentes.
- Manchas do fundo derivando devagar, sem parar.
- Painéis deslizando e escalando com curva suave.
- Um reflexo de luz atravessa a borda nos momentos-chave.
- Câmera com leve inclinação 3D.

## Som

Pads suaves, ambiente eletrônico, cliques de interface macios.

## Combina com / evite

| Combina com | Evite quando |
|---|---|
| apps, fintech moderna, tecnologia, música eletrônica, produto digital premium | texto longo, fundo chapado, marcas artesanais |

## Como fazer no estúdio

- **CSS:** `backdrop-filter: blur(20px); background: rgba(255,255,255,.15); border: 1px solid rgba(255,255,255,.35); border-radius: 24px`. O Chrome do HyperFrames e do Remotion renderiza o `backdrop-filter`.
- **After Effects/EffectCraft:** cópia do fundo com desfoque, recortada pela forma do painel (track matte), mais traço claro.
- O desfoque pesa no render: faça prévias em meia resolução.

## Para buscar referências

"glassmorphism UI", "frosted glass card", "glassmorphism motion", "iOS widgets glass".

## Armadilhas

- Texto com contraste baixo sobre o vidro.
- Fundo sem cor (o efeito não aparece).
- Painéis demais sobrepostos.
- Usado sem ideia, ele data a peça (moda de 2021).

## Exemplos salvos
