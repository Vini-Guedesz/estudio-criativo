# Adaptação do estúdio para canal dark

> Data: 2026-11-01 · Projeto: estudio-criativo

- **Pedido:** procurar skills de canal dark (fazer, manter, não perder alcance por conteúdo de IA), ler os repositórios a fundo e trazer só o que for relevante; depois subir o projeto numa branch nova com outro nome.
- **Feito:** análise em `03-referencias/analises/2026-11-01-skills-canal-dark.md`. Nova skill `.agents/skills/canal-dark/` (SKILL.md + references: politicas-ia, normas-do-canal, formatos, roteiro, visual, publicacao, crescimento, origem). Seção "Canal dark" em `06-metodo/regras.md`. Linhas novas nos roteadores `estudio-video` e `redes-sociais`, em `AGENTS.md` e no `README.md`. `02-ferramentas/voz.md` com a opção Kokoro (não instalada) e a regra do rótulo de IA. Créditos MIT em `TERCEIROS.md`.
- **Decisões:** nada de burlar detector, apagar C2PA ou publicar sem o dono; números de mercado sem fonte verificável ficaram de fora; motores próprios dos repositórios não entraram (o estúdio já tem HyperFrames, Remotion e EffectCraft); as regras de canais específicos viraram campos do modelo de normas.
- **Verificação:** regras do YouTube conferidas nas páginas oficiais em 01/11/2026; links e âncoras internos conferidos por script; `scripts/testar.py` não rodou porque nenhum script foi alterado e o ambiente (`.venv`) ainda não foi instalado. A skill ainda não foi usada num vídeo de verdade.
- **Próximo:** o dono escolhe o nome da branch e confirma o envio ao GitHub; instalar a voz Kokoro se quiser narração grátis; setup do estúdio (perfil, instalação, referências, marca do canal) segue pendente.
