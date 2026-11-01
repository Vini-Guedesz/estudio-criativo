# Voz e narração

> Data: 2026-11-01 · Tipo: guia · Status: instalado (Kokoro)

**Resumo:** a narração sai da sua voz gravada, de um clone da sua própria voz numa ferramenta de voz (ex.: ElevenLabs) ou de uma voz pronta de catálogo. O estúdio tem instalado o Kokoro, voz pronta em português do Brasil que roda no computador, de graça e sem conta, pelo script `scripts/som/narrar.py`.

## Kokoro (instalado)

- **O que é:** [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M), modelo aberto de voz, licença Apache-2.0 (uso comercial liberado). Não clona voz: só vozes prontas.
- **Vozes pt-BR:** `pf_dora` (feminina), `pm_alex` (masculina), `pm_santa` (masculina). Mistura de duas: `--voz "pm_alex,pm_santa"`. O site oficial não dá nota de qualidade para as vozes em português.
- **Instalação:** extra `voz` do `pyproject.toml`: `uv sync --extra gpu --extra voz` (com placa NVIDIA; sem placa, `--extra cpu --extra voz`). O português usa o espeak-ng que vem embutido no pacote `espeakng-loader`, sem instalar nada no Windows. O modelo (~330 MB) baixa sozinho no primeiro uso, no cache do Hugging Face.
- **Uso:**
  - `uv run scripts/som/narrar.py roteiro.md --voz pf_dora --saida <peça>/audio/narracao.wav`: uma frase por linha; linha em branco = pausa longa; linhas com `#` são ignoradas.
  - `--velocidade 0.95` deixa mais lento; `--texto "..."` narra uma frase solta.
  - `uv run scripts/som/narrar.py amostras --saida <pasta>` gera o mesmo texto nas 3 vozes, para comparar.
  - Ao fim, o script mostra a duração e as palavras por minuto: anote nas normas do canal.
- **Amostras:** `05-biblioteca/vozes/amostras/` (fora do git, como todo áudio).
- **Velocidade medida** (amostra de 79 palavras, velocidade 1.0): Dora 153, Alex 150, Santa 147 palavras por minuto.
- **Desempenho nesta máquina:** RTX 5060 8 GB, PyTorch 2.11 com CUDA 12.8; as 3 amostras de ~30 s saem em segundos.
- **Pronúncia:** nome estrangeiro sai soletrado ("McGill" virou "M. C. Gill"): escreva como se fala ("Mac Gil"). Números por extenso ("dois mil e onze") saem certos. Confira sempre com a transcrição.
- **Rótulo de IA no YouTube:** voz pronta que soa humana pede "Uso de IA: Sim". Marcar não reduz o alcance (skill `canal-dark`, `references/politicas-ia.md`).

## Outras opções

- **Gravar a própria voz:** celular a um palmo da boca, cômodo com cortina ou roupa, sem ventilador. Mande o arquivo para `04-marcas/<marca>/<tipo>/<peça>/audio/`.
- **Clonar a própria voz** (não instalado): [Chatterbox Multilingual](https://github.com/resemble-ai/chatterbox) (MIT, tem modelo pt-BR, clona com ~10 s de gravação e põe marca d'água inaudível em todo áudio) ou [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) (código Apache-2.0, clona com ~3 s). Clone da própria voz não precisa de rótulo de IA no YouTube. Só se clona a voz do dono, nunca a de outra pessoa.
- **ElevenLabs** (pago, na nuvem): a chave fica no gerenciador de senhas ou na configuração da ferramenta, nunca nesta pasta.

## Regras

- **Pronúncia:** escreva como se fala ("IÁ" para "IA") e confira com a transcrição (`uv run scripts/video/make_captions.py`). Regras de escrita para narração em `canal-dark/references/roteiro.md`.
- **Voz final:** seca, sem reverb nem eco; o volume é acertado na mixagem (`06-metodo/regras.md`).

## Log

- 2026-11-01: Kokoro instalado (extra `voz`), script `scripts/som/narrar.py` criado, amostras das 3 vozes pt-BR geradas e conferidas por transcrição. Opções de clone (Chatterbox, Qwen3-TTS) registradas.
