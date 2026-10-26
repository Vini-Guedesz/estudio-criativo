# Estilos: fichas de cada linguagem visual

> Data: 2026-10-25 · Tipo: entrada · Status: vigente

**Resumo:** uma ficha por estilo de arte, com o que faz o estilo ser reconhecido, paleta, fontes gratuitas, como se move, som, quando usar e como fazer no estúdio. A IA lê a ficha antes de propor uma direção visual e a pessoa usa para dar nome ao que gostou numa referência. Estilo novo nasce do [_modelo.md](_modelo.md).

## As fichas

| Estilo | Sensação | Combina com |
|---|---|---|
| [Pixel art](pixel-art.md) | nostalgia, humor, games | tecnologia, apps, marcas jovens |
| [Neobrutalismo](neobrutalismo.md) | direto, honesto, atrevido | SaaS jovem, criadores, educação |
| [Glassmorfismo](glassmorfismo.md) | leve, digital, premium | apps, fintech, música eletrônica |
| [Minimalismo suíço](minimalismo-suico.md) | rigor, clareza, autoridade | design, arquitetura, consultoria |
| [Clean tech](clean-tech.md) | limpo, confiável, moderno | tecnologia, produto, lançamentos (a base padrão do estúdio) |
| [Y2K](y2k.md) | divertido, pop, internet 2000 | moda, beleza, música |
| [Synthwave](synthwave.md) | noturno, energético, anos 80 | games, música, eventos |
| [VHS e lo-fi](vhs-lofi.md) | íntimo, nostálgico, caseiro | bastidor, streetwear, marca pessoal |
| [Flat ilustrado](flat-ilustrado.md) | claro, amigável, didático | explicativos, saúde, serviços |
| [3D clay](3d-clay.md) | fofo, cuidadoso, leve | apps de consumo, infantil, comida |
| [Colagem](colagem.md) | autêntico, cultural, artesanal | moda, música, causas, editorial |
| [Risografia](risografia.md) | independente, quente, impresso | cultura, cafés, livrarias |
| [Memphis](memphis.md) | alegre, enérgico, lúdico | eventos, festas, comida |
| [Tipografia cinética](tipografia-cinetica.md) | forte, ritmado, direto | frases, anúncios, aberturas |
| [Luxo escuro](luxo-escuro.md) | exclusivo, calmo, caro | joias, moda, perfumes, imóveis |
| [Doodle](doodle.md) | próximo, didático, pessoal | tutoriais, marca pessoal, educação |

## Como usar

- **Para dar nome ao que você gostou:** salve o link no mural (`03-referencias/mural.md` ou o da marca) e escreva o estilo na coluna "Estilo". Não sabe o nome? Deixe em branco: a IA identifica na análise.
- **Para começar uma marca ou uma peça:** peça "faz o pontapé inicial pelas referências". A IA segue a skill `referencias-e-estilos`: lê o mural, analisa os links, cruza com estas fichas e propõe direções.
- **Misturar estilos:** funciona com um estilo dominante e um de apoio. Exemplos: clean tech com toques de neobrutalismo (cards limpos com sombra sólida nos botões), tipografia cinética sobre VHS, doodle por cima de clean tech. Três estilos ao mesmo tempo costumam virar bagunça.
- **Modelo de post.** O gerador de post (`npm run post --prefix scripts/design -- --estilo <ficha>`) tem quatro modelos, e cada ficha usa o mais próximo: **limpo** (clean tech, glassmorfismo, flat ilustrado, 3D clay, doodle, colagem), **bloco** (neobrutalismo, Memphis, pixel art), **grade** (minimalismo suíço, tipografia cinética, risografia) e **escuro** (luxo escuro, synthwave, Y2K, VHS). Para o efeito completo do estilo (textura, ilustração, 3D), monte a peça em HTML e renderize com `scripts/design/render.py`.
- **A marca manda na paleta.** As cores das fichas são de partida. Na peça, o estilo empresta formas, tipografia e movimento, e as cores saem de `04-marcas/<marca>/identidade/design-tokens/marca.json` (ou são adaptadas a ela).

## Como criar uma ficha nova

1. Copie o [_modelo.md](_modelo.md) para `estilos/<nome-sem-acento>.md`.
2. Junte de 5 a 10 exemplos do estilo (mural ou catálogo) e preencha a partir deles, não da memória.
3. Acrescente uma linha na tabela acima.
4. Sempre que uma peça usar o estilo, cite o arquivo final em "Exemplos salvos" da ficha. Assim ela melhora com o uso.
