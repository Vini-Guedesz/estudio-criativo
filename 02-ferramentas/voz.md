# Voz e narração

> Data: 2026-11-01 · Tipo: guia · Status: não instalado

**Resumo:** a narração sai da sua voz gravada, de um clone da sua própria voz numa ferramenta de voz (ex.: ElevenLabs) ou de uma voz sintética de catálogo. O estúdio não instala nenhuma por padrão; quando você escolher uma, a IA atualiza este doc.

- **Gravar a própria voz:** celular a um palmo da boca, cômodo com cortina ou roupa, sem ventilador. Mande o arquivo para `04-marcas/<marca>/<tipo>/<peça>/audio/`.
- **Voz clonada:** crie a voz na ferramenta escolhida e guarde a chave no gerenciador de senhas ou na configuração da CLI dela, nunca nesta pasta. Só se clona a voz do dono, nunca a de outra pessoa.
- **Voz de catálogo local e grátis (opção para canal dark):** [Kokoro](https://huggingface.co/hexgrad/Kokoro-82M), modelo aberto que roda no computador, sem conta nem chave, com vozes em português do Brasil. Para português precisa também do [espeak-ng](https://github.com/espeak-ng/espeak-ng). O [explainroo](https://github.com/vincentsch/explainroo) (MIT) é um jeito pronto de usar o Kokoro com tempo de cada palavra. Ainda não instalado: peça "instala o Kokoro" e a IA instala, testa as vozes em português e atualiza este doc.
- **Rótulo de IA no YouTube:** clone da sua própria voz não precisa de rótulo; voz sintética que soa humana, marque "Uso de IA: Sim". Marcar não reduz o alcance. Detalhes na skill `canal-dark` (`references/politicas-ia.md`).
- **Pronúncia:** escreva como se fala ("IÁ" para "IA") e confira com a transcrição (`uv run scripts/video/make_captions.py`). Regras de escrita para narração em `canal-dark/references/roteiro.md`.
- **Voz final:** seca, sem reverb nem eco; o volume é acertado na mixagem (`06-metodo/regras.md`).
- **Log:**
  - 2026-11-01: acrescentadas a opção Kokoro e a regra do rótulo de IA (adaptação para canal dark).
