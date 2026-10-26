# 02-ferramentas: o que está instalado e como usar

> Data: 2026-10-26 · Tipo: entrada · Status: vigente

**Resumo:** um doc por programa, biblioteca ou serviço do estúdio, e a tabela de qual ferramenta usar para cada tipo de peça, para qualquer agente saber o que existe e escolher sem depender da memória da conversa. O `inventario.md` é gerado pelo `setup/conferir.py`; os outros docs a IA escreve e atualiza.

## Arquivos

| Arquivo | O que tem |
|---|---|
| `inventario.md` | Tabela gerada: cada ferramenta, versão e se está pronta. Rode `python setup/conferir.py` para atualizar |
| `<ferramenta>.md` | Um doc por ferramenta, no modelo abaixo |

## Qual ferramenta usar

Antes de produzir qualquer peça, a IA escolhe a ferramenta por esta tabela e diz ao dono qual vai usar e por quê. Confira o que está instalado no `inventario.md` (o PhotoCraft só fica ligado à IA na pasta onde o instalador rodou, pelo `.mcp.json`).

| A peça precisa de | Use | Por quê |
|---|---|---|
| Post e carrossel com a identidade da marca, em série | gerador de post (`npm run post --prefix scripts/design`) | lê fonte, cores, estilo e logo da marca; regera igual em segundos |
| Prova de direção, layout especial, mockup de tela | HTML + `scripts/design/render.py` (tela de app: skill `ui-para-video`) | controle total do layout; o mesmo HTML depois vira animação |
| Logo: símbolo, nome em curvas, versões | SVG + `scripts/design/logo.py`; acabamento de curvas no **Inkscape** | vetor limpo, sem depender da fonte instalada |
| Foto: retoque, recorte fino, cor, mockup com foto, abrir ou salvar `.psd` | **PhotoCraft** (recorte rápido: `scripts/design/sem_fundo.py`) | edição de imagem de verdade, em camadas |
| Ilustração ou pintura feita à mão | **Krita** (opcional, `-AppsDesign`) | pincel e camadas |
| Vídeo de tela, texto animado, legenda, peças em série | **HyperFrames** ou **Remotion** | fiel ao HTML aprovado; trocar texto e gerar outra versão é trivial |
| Motion com acabamento: molas orgânicas, desfoque de movimento real, brilho, câmera 3D, muitas camadas | **EffectCraft** (grátis) ou **After Effects** (se instalado) | curvas e efeitos de editor de motion; gera projeto que o dono pode abrir e ajustar |
| Edição de gravação longa (cortes, ordem das cenas) | `scripts/video/cut_pauses.py` + **DaVinci Resolve** (manual, opcional) | corte de pausa automático; edição fina na linha do tempo |

Regras de desempate:

- **Código** quando a peça se repete, precisa ser idêntica ao que foi aprovado ou ter números conferidos (contraste, tamanho, tempo).
- **Editor visual** (EffectCraft, PhotoCraft, Inkscape) quando o resultado pede acabamento manual ou o dono quer abrir o arquivo e mexer sozinho. Pergunte isso no critério de pronto.
- **Na dúvida entre dois motores de vídeo**, faça os mesmos 3 segundos nos dois e mostre lado a lado antes de seguir. A escolha e o porquê vão para o `06-metodo/escolhas.md`.
- Vídeo sempre começa pela skill `estudio-video`, que tem a escolha de motor em detalhe.

## Regra

Instalou, trocou de versão ou descobriu uma pegadinha? Atualize o doc da ferramenta na mesma sessão. Nunca escreva a chave, a senha ou o token: diga só onde ele está guardado.

## Modelo (`nome-da-ferramenta.md`)

```markdown
# Nome da ferramenta

> Data: AAAA-MM-DD · Tipo: guia · Status: vigente

**Resumo:** para que usamos, em uma frase.

- **Como acessar:** CLI, app, MCP ou biblioteca Python; onde roda.
- **Instalação:** o comando usado e a versão.
- **Credenciais:** onde estão guardadas (nunca o valor).
- **Comandos mais usados:** exemplos reais, para copiar e colar.
- **Pegadinhas:** limites, custo, o que quebra.
- **Log:** AAAA-MM-DD, o que mudou.
```
