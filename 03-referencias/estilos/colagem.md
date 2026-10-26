# Colagem e recorte

> Data: 2026-10-25 · Tipo: estilo · Status: vigente

**Resumo:** fotos recortadas, papel, fita adesiva e rabiscos sobrepostos, como um caderno ou zine. Passa autenticidade, cultura e mão humana.

## Como reconhecer

- Fotos recortadas com borda branca ou rasgada.
- Texturas de papel, fita adesiva, grampos.
- Mistura de foto em preto e branco com elementos coloridos.
- Letras recortadas de tamanhos e fontes diferentes.
- Rabiscos, setas e anotações à mão.
- Sobreposição e leve desalinhamento.

## Paleta

| Papel | Hex |
|---|---|
| Papel | kraft #D8C3A5 ou branco-papel #F3EFE6 |
| Base | preto #111111 |
| Acento (um) | vermelho #D62828 ou azul #002FA7 |

## Tipografia

DM Serif Display (títulos), Special Elite (máquina de escrever), Caveat (anotações). Letras recortadas como imagem, não como fonte.

## Forma, composição e textura

- Camadas sobrepostas com pequenas rotações.
- Sombra curta embaixo de cada recorte (papel sobre papel).
- Textura de papel por cima de tudo.

## Movimento

- Stop motion: 12 quadros por segundo (ou "de dois em dois"), mesmo num vídeo de 30.
- Recortes entram com pequeno giro e assentam.
- Linhas tremendo levemente em loop (boil).
- Papel deslizando, cortes no ritmo da música.

## Som

Papel, tesoura, fita sendo puxada, música analógica ou indie.

## Combina com / evite

| Combina com | Evite quando |
|---|---|
| cultura, moda, música, editorial, causas sociais, marcas autênticas e artesanais | tecnologia limpa, interface de produto |

## Como fazer no estúdio

- Recorte as fotos com `scripts/design/sem_fundo.py` e acrescente borda branca (stroke) no Figma, no PhotoCraft ou no CSS (`filter: drop-shadow`).
- Texturas de papel e fita em `05-biblioteca/assets/`.
- **After Effects:** `posterizeTime(12)` na expressão para o ritmo de stop motion.
- **HyperFrames:** `steps()` nas animações e pequenas rotações aleatórias fixas por elemento.

## Para buscar referências

"collage motion design", "paper cut out animation", "zine aesthetic", "mixed media collage".

## Armadilhas

- Poluição: deixe um ponto focal claro.
- Foto de terceiros recortada sem direito de uso.

## Exemplos salvos
