---
name: canal-dark
description: Canal dark (faceless, sem rosto) no YouTube e nos Shorts - criar o canal e as normas dele, escolher o formato (explicador "por quê", história de sobrevivência dia a dia, "E se...", bonequinho, documentário de curiosidades), pesquisar fontes, roteiro com retenção escrito para narração, imagens geradas e inserts desenhados por código, miniatura, título, descrição, capítulos, rótulo de IA, Short de chamada, cortes, auditoria do canal e "por que meu vídeo não decola". Usar sempre que o pedido for sobre canal dark, faceless, canal sem aparecer, vídeo narrado por IA para YouTube, monetização com vídeo de IA, conteúdo inautêntico ou reutilizado, ou como não perder alcance por usar IA, mesmo sem nomear a skill.
---

# Canal dark: fazer, manter e não perder alcance

> Data: 2026-11-01 · Tipo: guia · Status: vigente

**Resumo:** como o estúdio monta e toca um canal sem rosto no YouTube. O canal é uma marca em `04-marcas/<canal>/`, cada vídeo é uma peça (`videos/` para o longo, `reels/` para o Short) e a produção passa pelas skills que o estúdio já tem. O que derruba canal dark não é a IA ser detectada: é vídeo genérico, repetido ou enganoso. Então tudo aqui serve a três coisas: cada vídeo com pesquisa e ângulo próprios, o canal com uma identidade que se repete, e o dono aprovando o que sai com o nome dele.

## Primeiro, as regras do jogo

Leia [references/politicas-ia.md](references/politicas-ia.md) antes do primeiro vídeo de um canal. Em uma frase: o YouTube não pune o uso de IA; ele não paga por vídeo que parece feito em série, vídeo que reaproveita material alheio sem mudar de verdade, vídeo feito para chocar e "especialista" falso feito por IA em saúde, finanças, direito ou política. Marcar o vídeo como IA, quando é exigido, **não reduz o alcance** (palavras do próprio YouTube). Esconder a IA, apagar metadados ou burlar detector viola as regras das plataformas, e o estúdio não faz.

## Os pedidos e o caminho

| Pedido | O que fazer |
|---|---|
| "Quero criar um canal dark de..." | Seção **Criar o canal** abaixo |
| "Que formato eu uso?" / link de um vídeo para "fazer igual" | [formatos.md](references/formatos.md); o link vai para o mural e é analisado pela skill `referencias-e-estilos` (a gente estuda a mecânica, nunca copia texto nem imagem) |
| "Faz o vídeo de [tema]" | Seção **Produzir um episódio** abaixo |
| "Escreve o roteiro" | [roteiro.md](references/roteiro.md) |
| Imagens, miniatura, ritmo das cenas | [visual.md](references/visual.md) |
| Título, descrição, capítulos, tags, rótulo de IA, Short | [publicacao.md](references/publicacao.md) |
| "Por que não decola?", "analisa meu canal", plano do mês | [crescimento.md](references/crescimento.md) |
| Cortes de um vídeo longo em Shorts | [crescimento.md · cortes](references/crescimento.md#cortes-do-vídeo-longo) e skill `redes-sociais` |
| "Não vou perder monetização por usar IA?" | [politicas-ia.md](references/politicas-ia.md) e o checklist de originalidade |

## Criar o canal

O canal é do dono: o tema, o nome, a voz e a conta são dele. A IA propõe com um motivo e o dono decide. **Conversar não é aprovar:** uma pergunta ou um "o que você acha?" não é um sim. Cada decisão vai, com as palavras do dono e a data, para `04-marcas/<canal>/identidade/decisoes.md`.

1. **A marca.** Roteiro [setup/4-marca.md](../../../setup/4-marca.md): cria `04-marcas/<canal>/`, faz a entrevista e monta a identidade visual (avatar, banner, cores, fonte).
2. **O tema e o formato** ([formatos.md](references/formatos.md)). O tema é do dono. O formato diz como o vídeo se mexe (imagem parada com câmera, personagem, quadro-negro, colagem). Faça o teste do espelho antes de fechar o tema.
3. **As normas do canal.** Copie o [modelo](references/normas-do-canal.md) para `04-marcas/<canal>/identidade/normas-do-canal.md` e preencha com o dono: formato único, duração, estilo de imagem, molde de miniatura, molde de título, linhas vermelhas, se o canal exige fontes, voz, horário, configurações do Studio. O YouTube liga um canal a um público pelo que se repete; um vídeo fora da norma confunde esse sinal para todos os outros.
4. **A voz.** Só duas vozes servem: a do dono (gravada ou clonada da própria voz) ou uma voz sintética de catálogo. **Nunca a voz de outra pessoa**, nem que peçam. Opções e como instalar em [02-ferramentas/voz.md](../../../02-ferramentas/voz.md). Clonar a própria voz dispensa o rótulo de IA no YouTube; voz sintética realista pede o rótulo (ver políticas).
5. **O que só o dono faz no YouTube:** criar o canal, verificar por telefone (sem isso não tem miniatura própria nem vídeo acima de 15 minutos), aceitar termos, configurar credenciais. A IA prepara os passos e confere o resultado, nunca cria conta nem guarda senha.
6. **O plano** vai para o `calendario.md` da marca pela skill `redes-sociais`, com a cadência que a produção aguenta de verdade.

## Produzir um episódio

Cada vídeo é uma peça: `uv run scripts/peca.py nova videos "tema"` (o Short de chamada: `reels`). O método geral é o [video-do-zero](../../../06-metodo/video-do-zero.md). No canal dark ele ganha estas paradas, que são do dono e nunca da IA:

| Parada | O dono aprova | Antes de... |
|---|---|---|
| 0. Formato | nas normas do canal, uma vez | o primeiro vídeo |
| 1. Tema e ângulo | um de 3 ângulos propostos | pesquisar a fundo |
| 2. Roteiro | o texto que vai ser narrado, com as fontes ao lado | gerar voz e imagens |
| 3. Áudio | a narração inteira ouvida | montar |
| 4. Quadros | a folha de contato das imagens, antes do render final | renderizar |
| 5. Publicação | vídeo, miniatura e textos, no Studio | publicar |

A aprovação vale para aquele texto. Se o roteiro mudar depois de aprovado, a aprovação caiu: mostre de novo. Anote cada aprovação no `README.md` da peça com a data e as palavras do dono.

Os passos:

1. **Tema e ângulo.** Leia as normas do canal, o `calendario.md` e o `resultados.md` da marca. Não repita tema já feito. Proponha 3 ângulos de tipos diferentes; o dono escolhe.
2. **Fontes** em `fontes.md` na pasta da peça ([roteiro.md · fontes](references/roteiro.md#fontes)). Em canal que vive de fatos, tema sem fonte verificada não vira vídeo.
3. **Roteiro** em `roteiro.md` ([roteiro.md](references/roteiro.md)). A IA monta a estrutura e o rascunho a partir das fontes; o dono põe a opinião, a história ou o ângulo dele e aprova. É essa contribuição humana que separa o canal do conteúdo feito em série. Depois do rascunho, rode a revisão em duas etapas (revisor e refutador) da seção [revisar](references/roteiro.md#revisar-antes-de-mostrar), e a skill `humanizer` no texto.
4. **Narração** com a voz do canal, aprovada inteira antes de seguir. Legenda e tempo de cada palavra com `uv run scripts/video/make_captions.py`.
5. **Visual** ([visual.md](references/visual.md)): imagens geradas para as cenas e inserts desenhados por código para tudo que tem número, nome ou texto. Motor pela skill `estudio-video` (HyperFrames ou Remotion para montagem em código; EffectCraft ou After Effects para acabamento). Som pela `som-do-video`.
6. **Revisão** pelo checklist do `estudio-video` mais o [checklist de originalidade](references/politicas-ia.md#checklist-de-originalidade-antes-de-publicar).
7. **Publicação** ([publicacao.md](references/publicacao.md)): miniatura, 5 títulos, descrição, capítulos com os tempos reais, comentário fixado, ficha do Studio com o rótulo de IA certo e o Short de chamada. Textos na `copy.md` da peça. O dono publica.
8. **Números** 7 dias depois no `resultados.md` (skill `redes-sociais`) e o que aprendeu no `06-metodo/aprendizados.md`.

## O que o estúdio não faz

- Publicar sozinho ou subir vídeo sem o dono ver. Upload automático, no máximo, como rascunho privado.
- Clonar ou imitar o formato de um canal específico a ponto de parecer intercambiável, ou refazer o roteiro de outro vídeo.
- Baixar vídeo de outro canal para usar como material do nosso. Para estudar uma referência, a skill `watch` ou o `scripts/referencias.py` podem baixar uma cópia local de análise; nada dela entra no vídeo publicado.
- Inventar número, estudo, citação, depoimento ou resultado. Também não promete views, prazo ou monetização.
- Comprar views, inscritos ou likes; trocar o país do canal; VPN; encher de tags; título que o vídeo não cumpre.
- Apagar metadados de IA (C2PA), marca d'água ou rótulo, nem tentar enganar detector.
- Criar "médico", "advogado" ou "consultor financeiro" feito por IA dando conselho.

De onde veio cada parte desta skill, e o que ficou de fora: [references/origem.md](references/origem.md).
