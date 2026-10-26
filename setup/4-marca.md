# Roteiro 4: a marca do projeto

> Data: 2026-10-24 · Tipo: guia · Status: vigente

**Resumo:** instruções para a IA criar uma marca numa conversa: abre a pasta dela em `04-marcas/<marca>/`, preenche o `identidade/briefing.md`, transforma as respostas em identidade visual (cores, fontes, tokens) e, se a pessoa quiser, já cria as primeiras opções de logo, avatar e post. Serve para a primeira marca e para cada marca nova. Pronto quando o briefing da marca não tiver mais o marcador `BRIEFING-EM-BRANCO` e o `identidade/design-tokens/marca.json` dela não tiver mais a chave `_modelo`.

## Para a IA: como conduzir

Fale em português simples. É uma conversa de descoberta, não um formulário: a pessoa pode não saber responder tudo, e o seu papel é ajudar a pensar.

### 0. Antes de perguntar

1. **Abra a pasta da marca.** Pergunte o nome. Se ainda não houver, use um provisório (ex.: "Marca do Vini"); quando o nome for escolhido na etapa 2, rode `uv run scripts/peca.py renomear "Nome escolhido"`, que muda a pasta e os caminhos nos documentos. Crie com `uv run scripts/peca.py marca "Nome"`. Ele cria `04-marcas/<marca>/` com tudo no padrão de [04-marcas/_LEIA.md](../04-marcas/_LEIA.md). Daqui em diante, todo arquivo desta marca fica dentro dessa pasta.
2. Leia `01-sobre-mim/perfil.md`: não pergunte de novo o que já está lá.
3. Pergunte se a marca já existe (logo, site, perfil). Se existir e a pessoa permitir, olhe o material e já preencha o que der para deduzir; depois só confirme.
4. Peça de 5 a 10 links de referência (marcas admiradas, concorrentes, o estilo que ela quer) e 2 ou 3 do que a marca não pode parecer. Eles vão para o `04-marcas/<marca>/referencias/mural.md`. Leia também o catálogo e o mural geral de `03-referencias/`.

### 1. A entrevista

Siga as seções do briefing **na ordem**, em blocos de 2 ou 3 perguntas por mensagem. Regras:

- **Ofereça opções concretas** quando a pessoa travar (ex.: "ela é mais tipo Nubank, leve e direta, ou mais tipo Itaú Personnalité, séria e sofisticada?").
- **Aceite "não sei"**: anote como pendente e proponha uma hipótese baseada no resto.
- **Resuma ao fim de cada seção** em 2 linhas e peça um "ok".
- **Não pule público e posicionamento** (seções 2 e 3): são o que evita uma marca genérica.
- Não acrescente perguntas além das do briefing; o que der para deduzir, deduza e só confirme.
- Preencha o arquivo com as palavras da pessoa, troque a data, mude o status para `vigente` e apague as duas linhas de comentário do marcador `BRIEFING-EM-BRANCO`.

### 2. Nome (só se a marca ainda não tiver)

Faça esta etapa **depois** da entrevista, com todo o contexto em mãos.

1. **Gere de 10 a 15 nomes** em estilos diferentes, rotulados: descritivo (diz o que faz), metáfora (imagem que remete à essência), inventado (palavra nova e curta), composto (junção de duas palavras) e, se for marca pessoal, com o nome da pessoa. Para cada um, uma frase sobre a ideia por trás.
2. **Filtre** e mostre só os 5 melhores, com esta régua: fácil de falar e escrever depois de ouvir uma vez, curto, combina com a personalidade da seção 4, funciona no idioma do público, não lembra um concorrente da seção 3.
3. **Confira a disponibilidade** dos finalistas que a pessoa gostar:
   - **Marca parecida:** busca na web por marca igual ou parecida no mesmo nicho.
   - **Redes sociais:** para o @ principal e 2 variações (ex.: `nome`, `nome.oficial`, `usenome`), confira se já existe perfil ou página em:
     - Instagram: `https://www.instagram.com/<nome>/`
     - TikTok: `https://www.tiktok.com/@<nome>`
     - LinkedIn: `https://www.linkedin.com/company/<nome>/` (página de empresa) e busca por `site:linkedin.com "<nome>"`
     Abra os endereços (ou busque `site:instagram.com "<nome>"`, `site:tiktok.com "@<nome>"`). Essas redes costumam bloquear consultas automáticas ou pedir login: quando não der para confirmar, diga "não consegui verificar" e entregue os links prontos para a pessoa clicar. Nunca marque como livre o que não foi confirmado.
   - **Domínio:** `.com.br` e `.com` (busca na web ou registro.br).
   - Mostre o resultado numa tabela: nome × (marca parecida, Instagram, TikTok, LinkedIn, domínio) com ✅ livre, ❌ ocupado ou ❓ não verificado. Diga que é uma triagem, sem garantia.
4. A pessoa escolhe (ou pede outra rodada misturando os que gostou). Anote o nome na seção 1 e na seção 8 do briefing. Se a pasta nasceu com nome provisório, rode `uv run scripts/peca.py renomear "Nome"`.
5. Lembre, em uma linha, que antes de investir no nome vale buscar no INPI (busca.inpi.gov.br) e, se for usar comercialmente, registrar.

### 3. Plataforma da marca (síntese)

Com o briefing pronto, escreva `04-marcas/<marca>/identidade/plataforma.md` com: frase de posicionamento ("Para [público] que [necessidade], [marca] é [categoria] que [benefício]"), personalidade em 3 a 5 adjetivos com "somos / não somos", tom por situação, regras de escrita, 3 pares de exemplo (na voz / fora da voz) e pilares de conteúdo. O passo a passo está no guia de voz da skill `copy-redes` ([voz-da-marca.md](../.agents/skills/copy-redes/references/voz-da-marca.md)). Mostre e ajuste até a pessoa aprovar. Os pilares e o slogan, se houver, entram também no `calendario.md` e na seção 8 do briefing.

### 4. Identidade visual

1. **Moodboard:** faça o pontapé inicial da skill `referencias-e-estilos` com o mural da marca: analise as referências, dê nome aos estilos com as fichas de `03-referencias/estilos/` e proponha 2 ou 3 direções visuais (nome, conceito, estilo dominante e de apoio, paleta, fontes, movimento, as referências que sustentam cada uma), com um post e uma capa de Reels de prova em cada direção, salvos em `04-marcas/<marca>/identidade/direcoes/`. Registre cada rodada (direção e logo) no `06-metodo/escolhas.md`. As paletas das imagens saem com `uv run scripts/design/paleta.py <imagem>`.
2. **Cores:** para a direção escolhida, defina primária, secundária, fundo e texto (mais cores de apoio se precisar). Confira o contraste (texto ≥ 4.5) com `coloraide`.
3. **Fontes:** só fontes gratuitas para uso comercial (Google Fonts / Fontsource). Baixe os arquivos para `05-biblioteca/fontes/` e, se precisar no post, `npm install @fontsource/<fonte> --prefix scripts/design`.
4. **Tokens:** grave também o `estilo` (a ficha de `03-referencias/estilos/` da direção escolhida, que guia os posts) e a `secundaria-texto` se a cor secundária não tiver contraste para texto. Grave tudo em `04-marcas/<marca>/identidade/design-tokens/marca.json` (apague a chave `_modelo`) e rode `npm run tokens --prefix scripts/design -- --marca <marca>`.
5. Registre as decisões, com data, na seção 8 do briefing.

### 5. Primeiras peças (se a pessoa quiser agora)

- **Logo:** gere de 3 a 5 conceitos em SVG (código, Inkscape ou EffectCraft), cada um com a ideia em uma frase. Desenho à mão ou imagem de IA → `uv run scripts/design/vetorizar.py`. Conceitos em `identidade/logo/conceitos/`, uma folha por conceito com `uv run scripts/design/logo.py folha <simbolo.svg> --saida <png> --titulo "..." --ideia "..."` (símbolo, versão horizontal, foto de perfil, 64/32/20 px, versão com nome de cidade e negativo). No escolhido, `logo.py montar` gera cada versão com o nome em curvas (`--cidade` para a da cidade) e `logo.py perfil` a foto de perfil. Texto do logo final convertido em curvas. Versões finais em `04-marcas/<marca>/identidade/logo/` (horizontal, símbolo, monocromática, fundo claro e escuro) e `npm run svg --prefix scripts/design -- --marca <marca>` para otimizar.
- **Avatar:** DiceBear para rascunho (`npm run avatar --prefix scripts/design -- "semente" notionists --marca <marca>`), ilustração no Krita, 3D no Blender ou foto com `scripts/design/sem_fundo.py`. Final em `04-marcas/<marca>/identidade/avatar/`.
- **Post:** crie a peça (`uv run scripts/peca.py nova post "tema" --marca <marca>`) e gere com `npm run post --prefix scripts/design -- --peca <peça> "título" "apoio"` (layouts `capa`, `conteudo` e `cta`; ele lê fonte, cores, estilo e logo da marca). Confira a imagem antes de mostrar. O PNG vai para `rascunhos/` da peça, e o aprovado vai para `final/` com `uv run scripts/peca.py aprovar <arquivo>`. Modelos reutilizáveis ficam em `04-marcas/<marca>/modelos/`.
- **Vídeo:** HyperFrames e Remotion leem `04-marcas/<marca>/identidade/design-tokens/saida/marca.css`.

Mostre cada peça (abra a imagem), peça a escolha e só então siga.

### 6. Termine

1. Preencha o `README.md` da marca (o que faz, para quem, redes) e grave no ai-memory uma página durável com o resumo da marca (nome, pasta, posicionamento, cores hex, fontes, logo escolhido).
2. Registre a sessão em `anotacoes/`.
3. Diga o próximo passo: "peça o calendário do primeiro mês (skill `redes-sociais`) ou o primeiro post ou vídeo".
