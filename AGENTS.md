# Estúdio de IA: regras para o agente

> Data: 2026-10-22 · Tipo: entrada · Status: vigente

**Resumo:** instruções que o Claude Code e o Codex leem ao abrir esta pasta. A pasta é o segundo cérebro de quem cria vídeo com IA: guarda quem é o dono, as ferramentas instaladas, as referências, os projetos e o método. Leia este arquivo, depois o `01-sobre-mim/perfil.md`, e só então produza.

## Primeira vez nesta pasta

Esta pasta é um **modelo reutilizável**: cada projeto novo começa de uma cópia limpa. **Na primeira mensagem da sessão, antes de qualquer outra tarefa,** confira o estado e, se algo estiver pendente, cumprimente, diga em uma linha o que falta e ofereça começar pelo primeiro item pendente:

| Pendente se... | Roteiro |
|---|---|
| `01-sobre-mim/perfil.md` tem o marcador `PERFIL-EM-BRANCO` ou não existe `.ai-memory.toml` | [setup/1-segundo-cerebro.md](setup/1-segundo-cerebro.md): liga a memória (ai-memory) e faz a entrevista sobre a pessoa |
| não existe `.venv/` ou `scripts/design/node_modules/` | [setup/2-instalar.md](setup/2-instalar.md): programas, bibliotecas, skills, motores de vídeo e ferramentas de design |
| `03-referencias/ONDE.md` não existe ou ainda tem a data `AAAA-MM-DD` | [setup/3-referencias.md](setup/3-referencias.md): pasta de referências, local ou no Google Drive |
| `04-marcas/` não tem nenhuma marca (só as pastas `_modelo-*`) ou o `identidade/briefing.md` dela tem o marcador `BRIEFING-EM-BRANCO` | [setup/4-marca.md](setup/4-marca.md): cria a pasta da marca, faz a entrevista e monta a identidade visual |

Se a pessoa pedir outra coisa primeiro, atenda e lembre do pendente no fim.

## Como trabalhar com o dono do estúdio

1. **Combine o "pronto" antes de começar.** Se o pedido não diz quando a tarefa termina, pergunte uma vez, no início, com opções concretas. Depois disso, resolva sozinho o que conseguir resolver.
2. **O pedido já é a autorização** para o que a tarefa exige: rodar scripts, instalar bibliotecas, abrir programas, chamar ferramentas.
3. **Obstáculo não é motivo para parar.** Erros e ferramentas que falham fazem parte do trabalho: tente outro caminho antes de declarar bloqueio.
4. **Pare só quando:** o passo exigir senha, código 2FA, captcha ou cartão (deixe tudo pronto e avise em uma linha); a ação for destrutiva e o pedido não a cobrir; ou chegar a hora de uma aprovação que faz parte do processo (ex.: o áudio antes da edição).
5. **Fale em português simples.** Explique os termos necessários e mostre o que foi feito, o resultado e o próximo passo.
6. **Termine de verdade:** confira o resultado real (assista ao render, ouça o áudio), corrija o que falhar e registre o que fez.

## Onde cada coisa vive

| O quê | Onde |
|---|---|
| Ideia crua, ditado, print solto | [00-entrada/](00-entrada/_LEIA.md) |
| Quem é o dono, nicho, tom, objetivos | [01-sobre-mim/perfil.md](01-sobre-mim/perfil.md) |
| Um doc por programa, biblioteca ou serviço instalado | [02-ferramentas/](02-ferramentas/_LEIA.md) |
| Referências (vídeos, prints, estilos, sons, marcas), o mural de links e as fichas de estilo | [03-referencias/](03-referencias/_LEIA.md): [mural.md](03-referencias/mural.md) e [estilos/](03-referencias/estilos/_LEIA.md); se a mídia estiver no Google Drive, o caminho está em [03-referencias/ONDE.md](03-referencias/ONDE.md) |
| **Tudo de cada marca:** identidade, logo, avatar, cores, referências da marca, modelos e todas as peças (reels, posts, carrosséis, stories, vídeos) | [04-marcas/](04-marcas/_LEIA.md) |
| Música, efeitos sonoros, fontes e assets reutilizáveis | [05-biblioteca/](05-biblioteca/_LEIA.md) |
| Método de vídeo, números que valem e aprendizados | [06-metodo/](06-metodo/_LEIA.md) |
| Scripts de áudio, vídeo, design e revisão | [scripts/](scripts/_LEIA.md) |
| Registro de cada sessão | [anotacoes/](anotacoes/_LEIA.md) |
| Skills (motion, som, referências, texto e planejamento de redes) | `.agents/skills/` (o `.claude/skills` aponta para a mesma pasta) |

## Regras de trabalho

- **Toda peça mora na marca dela, no padrão de [04-marcas/_LEIA.md](04-marcas/_LEIA.md).** Crie com `uv run scripts/peca.py nova <tipo> "tema"` antes de produzir. Render, exportação e post gerado vão direto para `rascunhos/` da peça, com o nome que `peca.py rascunho` der. `final/` só recebe o que o dono aprovou, pelo `peca.py aprovar`. Nunca salve peça em outro lugar (pasta solta, área de trabalho, pasta do motor).
- **Texto de redes é da `copy-redes`; plano e números, da `redes-sociais`.** Legenda, gancho e carrossel vão para o `copy.md` da peça; o calendário e os resultados, para `calendario.md` e `resultados.md` da marca. Nenhum número, depoimento ou resultado inventado.
- **Escolha a ferramenta pela tabela de [02-ferramentas/_LEIA.md](02-ferramentas/_LEIA.md#qual-ferramenta-usar)** (código, Inkscape, PhotoCraft, HyperFrames, Remotion, EffectCraft, After Effects) e diga ao dono qual vai usar e por quê. Nada de animador ou editor improvisado quando o estúdio já tem a ferramenta.
- **Vídeo começa em [06-metodo/video-do-zero.md](06-metodo/video-do-zero.md).** Os números (mola, câmera, volume, render) moram só em [06-metodo/regras.md](06-metodo/regras.md); se outro doc trouxer um número diferente, vale o desse arquivo.
- **Referência antes de produzir.** Antes de animar ou gerar imagem, procure em `03-referencias/`, no mural e em `referencias/` da marca e na biblioteca, e leia a ficha do estilo em `03-referencias/estilos/`. Marca ou peça sem direção visual começa pelo pontapé inicial da skill `referencias-e-estilos`. Sem referência, o resultado sai genérico.
- **Todo insumo analisado vira doc.** Link, vídeo, post, site ou print que você analisou ganha um doc em `03-referencias/analises/`, detalhado o bastante para ninguém precisar reabrir a fonte.
- **Ferramenta nova entra no cérebro.** Instalou algo? Crie ou atualize o doc dela em `02-ferramentas/` (modelo no `_LEIA.md`) na mesma sessão.
- **Toda sessão termina com uma anotação** em `anotacoes/AAAA-MM/` (método no `_LEIA.md` da pasta).
- **Nenhuma credencial em arquivo.** Chave de API, senha e token ficam no gerenciador de senhas ou na configuração da própria ferramenta. Os docs dizem onde a chave está, nunca o valor.
- **Mexeu em script, rode o teste.** Depois de alterar qualquer arquivo de `scripts/` ou `scripts/design/`, rode `uv run scripts/testar.py` e só entregue com tudo ok.
- **Mudanças cirúrgicas.** Mexa só no que o pedido exige e siga o `_LEIA.md` de cada pasta.
- **Todo `.md` começa do mesmo jeito:** título, a linha `> Data: AAAA-MM-DD · Tipo: <tipo> · Status: <status>` e um resumo de 1 a 3 frases.

## Memória

A memória entre sessões e entre agentes (Claude Code e Codex) é o **ai-memory**, ligado pelo roteiro 1. Fatos duráveis, regras aprendidas e decisões vão para ele. Não guarde fatos do projeto na memória nativa de um agente só: o outro não a enxerga. O próprio setup acrescenta o bloco de instruções do ai-memory ao fim deste arquivo.
