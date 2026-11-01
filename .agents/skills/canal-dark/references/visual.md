# Visual de canal dark

> Data: 2026-11-01 · Tipo: guia · Status: vigente

**Resumo:** como sai a parte visual: imagens geradas para as cenas, inserts desenhados por código para tudo que leva número ou texto, o ritmo entre os dois e a miniatura. O estilo vem das normas do canal e da ficha em `03-referencias/estilos/`. O motor é escolhido pela skill `estudio-video`; o acabamento de movimento segue a `motion-narrado` e os números de [regras.md](../../../../06-metodo/regras.md).

## Quem desenha o quê

| O plano tem... | Quem faz | Por quê |
|---|---|---|
| Personagem, lugar, cena, objeto com textura | imagem gerada (PhotoCraft ou a ferramenta de imagem do dono) | é onde a IA é boa |
| Número, gráfico, linha do tempo, placar, comparação, título de capítulo, nome, mapa com rótulo, ícone sozinho | **código** (HyperFrames, Remotion ou HTML capturado) | sai exato, de graça e igual ao que a voz diz. IA erra letra e número |
| Foto de arquivo, documento, mapa histórico | imagem real com licença | dá credibilidade; licença anotada no `README.md` da peça |

O número na tela é **idêntico** ao número falado.

## Prompt de imagem

- **Nomear desenha.** Num prompt não existe palavra neutra: negação e medida também são menção. "Uma praça vazia" desenha alguém na praça; "do tamanho de duas mãos" desenha mãos. Descreva o que **existe** ("o chão de pedra aparece pelos três buracos") e meça em números ("1,5 m de altura").
- **Sem texto na imagem gerada.** Evite palavras que puxam letra: placa, cartaz, rótulo, mapa, tela mostrando, livro aberto, frasco etiquetado. Objeto que teria texto vira "liso, sem marcas". Texto entra depois, por código.
- **Sem código de cor no prompt** (hex, RGB, Pantone). Use nomes comuns: vermelho vivo, azul elétrico, dourado quente. No máximo três cores de destaque.
- **Âncora do personagem repetida igual.** O texto que descreve o personagem (traço, roupa, proporção) está nas normas do canal e vai **inteiro** em toda imagem. Nunca "o mesmo personagem de antes". O que muda é a ação e o lugar, descritos à parte.
- **Personagem sempre fazendo algo concreto** (abre, empurra, desenha, carrega). Nada de forma abstrata se derretendo em outra.
- **O prompt nasce do roteiro, mas não é o roteiro.** Ele descreve o que se vê naquela frase, não repete a frase.
- **O prefixo de estilo descreve só o acabamento** (traço, papel, paleta, luz). Objeto citado no prefixo aparece em todas as imagens.
- **Para corrigir uma imagem, mude o texto e mantenha a semente**, para a diferença ser do texto e não do acaso. Compare sementes só depois do texto acertado.
- **Uma geração por plano.** O que não chegar ao padrão fica anotado, e o dono decide na parada dos quadros. Nada de gerar dez vezes "até ficar bom" sem dizer.

## Ritmo do vídeo em imagens

Medido em 30 vídeos de explicador (terceiros, faceless-video-skills). Ponto de partida:

- **Uma imagem por frase**, de 3 a 6 s na tela, com corte seco. Uma cena pode durar 2 a 3 frases.
- Alterne: cena, insert, cena. Nunca mais de 2 inserts da mesma família em sequência, nem 3 inserts sem uma cena.
- Um insert de dado pelo menos a cada ~14 imagens, nunca dois seguidos.
- A imagem da abertura volta no meio e no fim.
- Pelo menos um plano em primeira pessoa e um de cima, para variar o ponto de vista.
- Imagem parada não precisa ficar morta: uma deriva lenta de câmera resolve (regra "câmera nunca morta" do regras.md). Se o formato do canal é corte seco sem movimento, isso está escrito nas normas.

## Revisão antes do render final (parada 4)

Monte a folha de contato (`uv run scripts/referencias.py olhar <arquivo>` num render de prévia, ou uma grade das imagens) e confira com o dono:

- Olhando só a imagem, sem som, dá para saber do que a frase fala?
- O personagem e os objetos mantêm tamanho e forma de uma imagem para a outra? Escala errada é o defeito que mais passa batido.
- Tem duas imagens quase iguais? Alguma foge do estilo?
- Alguma imagem tem letra, número ou bolha de fala que não devia?
- Alguma cruza as linhas vermelhas do canal (postura, violência, o que for)?

## Miniatura

- **Molde fixo do canal** (normas): mesmo personagem ou mascote, mesma faixa e cor de texto. Um canal com miniaturas de cara diferente perde o reconhecimento.
- **2 a 4 palavras, escritas por código**, nunca pelo gerador de imagem. Um número verdadeiro ou uma pergunta. Nunca um número que pareça duração ("3:47"), que se confunde com o relógio do YouTube.
- **Gramática revisada.** Texto curto engana: passe por um revisor (subagente) antes de fechar, ainda mais em outro idioma.
- **Não repita o título.** A miniatura é a emoção e o objeto; o título é a promessa e a palavra-chave.
- **Uma emoção forte, um objeto que diz o tema, 30 a 40% de espaço vazio**, um ponto de foco, contraste alto.
- **Teste no tamanho do celular** antes de aprovar.
- **Fiel ao vídeo.** Nada que o vídeo não mostre: o YouTube compara miniatura e título com o conteúdo.
- Tamanho e formato em [regras.md](../../../../06-metodo/regras.md#canal-dark). O teste A/B de miniatura (até 3 versões, no Studio pelo computador) vale a pena a partir dos primeiros vídeos com impressões.
