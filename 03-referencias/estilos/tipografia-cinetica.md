# Tipografia cinética

> Data: 2026-10-25 · Tipo: estilo · Status: vigente

**Resumo:** o texto é a imagem. Palavras grandes ocupam a tela e mudam de tamanho, peso e posição no ritmo da fala ou da música. Funciona quando há pouca imagem e uma mensagem forte.

## Como reconhecer

- Palavras enormes ocupando o quadro.
- Mudança de tamanho, peso e cor no tempo da fala.
- Uma palavra-chave destacada por frase.
- Contraste alto, poucas cores.
- Cortes rápidos entre frases.

## Paleta

Preto e branco com um acento (amarelo #FFE600, vermelho #FF3B30 ou a cor da marca).

## Tipografia

Anton, Bebas Neue, Archivo Black ou Inter Tight (fonte variável ajuda a animar o peso). Uma família só.

## Forma, composição e textura

- O texto preenche a largura útil (dentro da área segura do `regras.md`).
- Linhas empilhadas com entrelinha justa.
- Às vezes uma imagem pequena entra entre as palavras.

## Movimento

- Palavra por palavra no tempo da fala.
- Escala, máscara, giro de 90° na troca de frase.
- Câmera viajando pelo texto.
- Tempo de leitura: siga a regra de legenda da skill `motion-narrado`. Rápido demais fica ilegível.

## Som

Narração forte ou música com batida clara. Um golpe sonoro na palavra-chave.

## Combina com / evite

| Combina com | Evite quando |
|---|---|
| frases, citações, anúncios curtos, aberturas, opinião, pouca imagem disponível | conteúdo que precisa mostrar produto ou interface |

## Como fazer no estúdio

- Tempos por palavra: `uv run scripts/video/make_captions.py <audio> legendas.json`.
- Monte no HyperFrames ou no Remotion lendo esse JSON.
- Blocos prontos de texto cinético: skill `hyperframes-registry`.

## Para buscar referências

"kinetic typography", "kinetic type reel", "typography motion design", "text animation reels".

## Armadilhas

- Rápido demais para ler.
- Efeito em toda palavra: destaque só a palavra-chave.
- Fontes demais.

## Exemplos salvos
