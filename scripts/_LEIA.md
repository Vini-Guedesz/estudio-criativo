# scripts: as ferramentas de som, vídeo e referências

> Data: 2026-10-22 · Tipo: entrada · Status: vigente

**Resumo:** scripts que as skills chamam. Todos rodam da raiz do estúdio: os Python com `uv run`, que usa o `.venv` certo sozinho, e os de design em Node com `npm run <comando> --prefix scripts/design`. Cada um tem `--help` ou explica o uso no topo do arquivo.

## Marcas e peças

O padrão completo está em [04-marcas/_LEIA.md](../04-marcas/_LEIA.md).

| Comando | O que faz |
|---|---|
| `uv run scripts/peca.py marca "Nome"` | cria `04-marcas/<marca>/` a partir do modelo |
| `uv run scripts/peca.py renomear "Nome novo"` | troca o nome da marca: pasta, caminhos nos documentos e título da ficha |
| `uv run scripts/peca.py nova <tipo> "tema"` | cria a peça (`reels`, `videos`, `stories`, `posts`, `carrosseis`) com as pastas certas |
| `uv run scripts/peca.py rascunho <peça> <ext>` | caminho do próximo rascunho (`tema-reels-v2.mp4`): renderize direto nele |
| `uv run scripts/peca.py aprovar <rascunho>` | copia para `final/` com o nome limpo e anota no README da peça |
| `uv run scripts/peca.py lista` | marcas e peças |

## Design

Rodam da raiz. Os Node leem as cores e fontes de `04-marcas/<marca>/identidade/design-tokens/marca.json`. Com mais de uma marca, passe `--marca <nome>`.

| Comando | O que faz |
|---|---|
| `npm run post --prefix scripts/design -- --peca <peça> "Título" "apoio"` | post 1080x1350 com a identidade da marca (fonte, cores por contraste, logo) no `rascunhos/` da peça. `--layout capa\|conteudo\|cta`, `--estilo <ficha>`, `--numero`, `--rotulo`, `--parte N` |
| `npm run avatar --prefix scripts/design -- "semente" notionists` | avatar SVG (DiceBear) em `identidade/avatar/` |
| `npm run tokens --prefix scripts/design` | exporta cores e fontes para `identidade/design-tokens/saida/` (CSS e JSON) |
| `npm run svg --prefix scripts/design` | otimiza os SVGs de `identidade/logo/` em `logo/otimizado/` |
| `uv run scripts/design/logo.py montar <simbolo.svg> --saida <svg>` | símbolo + nome da marca em curvas, na fonte da marca (`--cidade "Nome"` para a versão da cidade) |
| `uv run scripts/design/logo.py folha <simbolo.svg> --saida <png>` | folha de um conceito de logo: grande, horizontal, cidade, perfil, 64/32/20 px e negativo |
| `uv run scripts/design/logo.py perfil <simbolo.svg> --saida <png>` | foto de perfil 1080x1080 |
| `uv run scripts/design/render.py <arquivo.html> --tamanho post\|reels\|LxA --saida <png>` | HTML em imagem (provas de direção, telas), esperando as fontes |
| `uv run scripts/design/vetorizar.py logo.png` | PNG → SVG (vtracer), ao lado do original. `--pb` para preto e branco |
| `uv run scripts/design/paleta.py ref.jpg` | paleta de uma referência + contraste |
| `uv run scripts/design/sem_fundo.py foto.jpg` | remove o fundo (rembg), ao lado do original; `birefnet-general` como 2º argumento para recorte fino |

## Referências

| Comando | O que faz |
|---|---|
| `uv run scripts/referencias.py novos` | lista o que chegou em `_entrada/` e baixa os links de `03-referencias/_entrada/links.md` |
| `uv run scripts/referencias.py olhar <arquivo>` | folha de contato com 16 quadros e o tempo de cada um |
| `uv run scripts/referencias.py mover <arquivo> <categoria> --tags "..." --nota "..."` | renomeia, move e registra no catálogo |
| `uv run scripts/referencias.py capturar <url>` | tela do site, no desktop e no celular, para a `_entrada/` (fecha o aviso de cookies) |
| `uv run scripts/referencias.py mural [--baixar]` | links salvos nos murais por status; `--baixar` baixa os vídeos e imagens novos |
| `uv run scripts/referencias.py criar` | cria as pastas das categorias onde a mídia fica (local ou Drive) |

## Vídeo

| Comando | O que faz |
|---|---|
| `uv run scripts/video/make_captions.py <video> legendas.json` | legenda palavra por palavra (JSON para Remotion e SRT) com o faster-whisper |
| `uv run scripts/video/cut_pauses.py <entrada> <saida>` | corta as pausas da fala sem mudar a velocidade |
| `uv run scripts/video/olho_quadro_a_quadro.py camera\|folha\|rastro\|ampliar\|compara ...` | mede câmera, amplia detalhes e compara a referência com a recriação |
| `uv run scripts/video/detectar_saltos.py <video>` | depois de todo render: acha quadros pulados, vazios ou isolados |

## Som

Os detalhes e o método estão na skill `som-do-video` e no [README da biblioteca de som](../05-biblioteca/som/README.md).

| Comando | O que faz |
|---|---|
| `uv run scripts/som/sintetizar_sfx.py` | gera a biblioteca inicial de efeitos (o instalador já roda) |
| `uv run scripts/som/nivelar.py <pasta>` | nivela um pack de efeitos seu no padrão do estúdio e cataloga o pico de cada um |
| `uv run scripts/som/som.py --eventos eventos.json ...` | gera a mixagem (efeitos, voz, música) a partir dos eventos da animação |
| `uv run scripts/som/verificar_som_de_cena.py <mix>` | reprova som de cena alto demais antes da entrega |
| `uv run scripts/som/batida.py <musica>` | batidas, tempos fortes e BPM (precisa da IA de áudio) |
| `uv run scripts/som/separar.py <musica>` | separa voz e instrumental (precisa da IA de áudio) |

## Teste automático

`uv run scripts/testar.py` cria uma marca temporária, exercita as regras de nome (iguais em Python e Node), marcas, peças, rascunhos, aprovação, post, tokens, mural e renomear, e apaga tudo no fim. Rode depois de mexer em qualquer script; ele sai com erro se algo falhar.

## Para quem escreve scripts novos

Use `scripts/_estudio.py` para achar as pastas (`RAIZ`, `SFX`, `MUSICA`, `midia_referencias()`, `marca()`, `peca()`, `rascunho()`), nunca caminho fixo. Script que gera arquivo de uma peça salva em `rascunho(peca, ext)`. Nos scripts Node, o mesmo vale para o `scripts/design/estudio.mjs`. Biblioteca nova entra no `pyproject.toml`, seguida de `uv sync`. Regra nova de nome ou caminho entra no `_estudio.py` e no `scripts/design/estudio.mjs`, e ganha um item no `scripts/testar.py`.
