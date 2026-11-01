# Formatos de canal dark

> Data: 2026-11-01 · Tipo: guia · Status: vigente

**Resumo:** os formatos que o estúdio sabe fazer, com a mecânica de cada um, o teste para escolher o tema e o motor que monta. O formato diz como o vídeo se mexe e como a história anda; a cara (estilo, cores, letra) é identidade do canal e fica nas normas. Formato novo fora desta lista: estude a referência com a skill `referencias-e-estilos`, descreva o que vê e proponha ao dono antes de construir.

## Escolher o tema: o teste do espelho

Um tema funciona quando a pessoa **se reconhece nele**: algo que ela tem, faz, sente ou já se perguntou ("por que a gente sente arrepio", "e se você ficasse preso num bunker"). Antes de fechar um tema, três perguntas:

1. A pessoa pode olhar no espelho, ou para o próprio dia, e achar o assunto?
2. A resposta conhecida está errada ou incompleta, ou existe uma pergunta que todo mundo já se fez?
3. Existem fontes que sustentam a explicação?

Duas respostas "não" = troque o tema. Medição de terceiros (faceless-video-skills, um canal de evolução humana, 29 vídeos): temas em que a pessoa se reconhece tiveram mediana dez vezes maior que temas médicos ou abstratos. Use como pista, não como lei; o `resultados.md` do canal manda.

## Os formatos

### 1. Explicador "por quê" (paradoxo + ciência)

Um paradoxo que a pessoa carrega no corpo ou no dia, explicado com nomes, datas e números, e virado do avesso no fim ("não era defeito, era uma troca").

- **Duração:** 4 a 7 min (padrão 5).
- **Visual:** uma imagem por frase, parada, com cortes secos; inserts por código para números e nomes.
- **Estrutura:** os 8 tempos de [roteiro.md](roteiro.md#explicador-os-8-tempos).
- **Título:** pergunta ou "Por que [força] fez seu [traço]...".
- **Motor:** HyperFrames ou Remotion montando imagens + inserts sobre a narração.

### 2. História de sobrevivência dia a dia (segunda pessoa)

"Você está preso num bunker por um ano." Diário em segunda pessoa, com relógio, inventário, crises e um mistério.

- **Duração:** 10 a 12 min.
- **Estrutura:** a folha de ritmo de [roteiro.md](roteiro.md#história-de-sobrevivência-a-folha-de-ritmo).
- **Regra de ouro:** números que dá para recalcular (litros, calorias, dias) e crises resolvidas em passos, com uma lição e uma regra nova.
- **Variedade:** troque cenário, ameaça, crise e reviravolta a cada episódio (inverno nuclear, ilha, estação polar, submarino...).

### 3. "E se..." (hipótese universal)

"E se duas pessoas tivessem que recomeçar a humanidade?" Mesma mecânica do explicador (cena, fatos, fontes), mas com uma hipótese no lugar do paradoxo.

- **Duração:** 6 a 9 min; funciona em série de 3 partes quando um vídeo decola.
- **Cuidado:** hipótese é ficção apoiada em fatos. O roteiro separa claramente o que é dado ("a população mínima estimada em estudos é...") do que é imaginação ("imagine que...").

### 4. Bonequinho (stickman) narrado

Personagem de traço simples com expressão forte, em ilustração com microanimação. Serve para psicologia, trabalho, negócios, histórias.

- **Duração:** Short de 30 a 60 s ou vídeo de 3 a 10 min.
- **Estrutura:** o arco em 5 etapas de [roteiro.md](roteiro.md#arco-em-5-etapas-curtos-e-bonequinho).
- **Regra visual:** o texto âncora do personagem é repetido **igual** em toda imagem gerada; nada de "o mesmo personagem". Duas pernas, dois braços, proporção fixa. Personagem nunca parado: sempre fazendo uma ação concreta.

### 5. Documentário de curiosidades e história

Lugares, objetos, eventos, empresas. Exige mais pesquisa e mais imagem real (fotos de arquivo, mapas, documentos).

- **Duração:** 8 a 20 min.
- **Imagem real:** foto de arquivo e mapa com licença conhecida (domínio público, Wikimedia com crédito, acervo oficial), anotada no `README.md` da peça. Reconstituição feita por IA de evento real e realista **pede rótulo de IA**.
- **Base:** skill `video-referencias` (assets reais do assunto) e `motion-narrado`.

### 6. Short de chamada e Shorts próprios

- **Short de chamada:** os primeiros 35 a 55 s do vídeo longo (abertura + crença errada + promessa), terminando na pergunta em aberto, ligado ao vídeo longo por "Vídeo relacionado". Receita em [publicacao.md](publicacao.md#short-de-chamada).
- **Short próprio:** gancho já montado no quadro 0 (sem surgir do preto), revelação em 2 a 4 passos e último quadro igual ao primeiro, para dar loop. Termine na revelação, sem "comenta aí".

## O que fica fixo e o que varia

| Fixo no canal (normas) | Varia a cada vídeo |
|---|---|
| formato, duração, estrutura | tema, época, lugar |
| estilo das imagens, personagem âncora | cenas, ações, cenários |
| molde de miniatura e de título | as palavras, o objeto, a emoção |
| voz, tom, horário | a história, o desfecho, a conclusão |

Se dois vídeos seguidos só trocam a palavra-chave, a variação falhou: é exatamente o que a política chama de "personagens na mesma situação com o mesmo desfecho".
