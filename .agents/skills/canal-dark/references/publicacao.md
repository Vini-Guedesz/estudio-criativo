# Publicação de canal dark

> Data: 2026-11-01 · Tipo: guia · Status: vigente

**Resumo:** o kit que todo vídeo entrega para o dono publicar no YouTube Studio: miniatura, 5 títulos, descrição, capítulos, comentário fixado, ficha de configuração e checklist. Os textos vão para a `copy.md` da peça (skill `copy-redes` para o tom), a miniatura e o Short saem em `rascunhos/` e, aprovados, em `final/` pelo `scripts/peca.py aprovar`. O estúdio nunca publica: no máximo deixa um rascunho privado.

## Quando montar

Depois que o dono aprova o vídeo final. Se ele pedir antes, monte a partir do roteiro aprovado e marque como **rascunho**: capítulos, conferência da miniatura com o corte final e licenças ficam pendentes.

## O kit

1. **Miniatura** 1280x720 (ou 1920x1080), menos de 2 MB, pelo molde do canal ([visual.md](visual.md#miniatura)). Conferida no tamanho do celular.
2. **5 títulos diferentes:** um de busca (palavra-chave na frente), um de curiosidade, um amplo, e dois pelo molde do canal. Até 60 caracteres, contados por código (`len()`), com o gancho nos primeiros ~45. Nenhum número sem fonte, nenhuma promessa que o vídeo não cumpre. Marque o recomendado.
3. **Descrição:**
   - as 2 primeiras linhas são um segundo gancho (só ~150 caracteres aparecem antes do "mais"); nada de "olá, pessoal";
   - os capítulos;
   - um parágrafo com o tema em linguagem natural (a palavra-chave aparece 2 a 4 vezes, sem encher);
   - **fontes** (as do `fontes.md`) e créditos de música, imagens de arquivo e efeitos;
   - links verdadeiros (playlist, vídeo anterior); nenhum link inventado;
   - 3 hashtags no fim (com mais de 15, o YouTube ignora todas).
4. **Capítulos** com os tempos **reais** da narração (da transcrição do `make_captions.py`), nunca estimados do roteiro: o primeiro em 0:00, pelo menos 3, cada um com 10 s ou mais. Nome de momento forte, com a palavra-chave quando couber.
5. **Comentário fixado:** a pergunta do fim do vídeo, numa linha. Sem polêmica fabricada.
6. **Tags:** quase não pesam. Só erros de digitação comuns do tema e desambiguação, até 500 caracteres.
7. **Ficha de configuração** (abaixo).
8. **Checklist** (abaixo), cada item marcado como feito, pendente ou não se aplica.

## Ficha de configuração do Studio

Copie para a `copy.md` da peça e preencha pelas normas do canal:

```markdown
## Publicação

| Campo | Valor |
|---|---|
| Título escolhido | … |
| Categoria | … (a mesma em todo o canal) |
| Idioma do vídeo e dos metadados | … |
| Feito para crianças | Não (se marcado "sim", somem comentários, tela final e boa parte das recomendações) |
| Uso de IA (rótulo) | Sim / Não, e por quê (politicas-ia.md) |
| Comentários | ativados |
| Playlist | … |
| Tela final | inscrever-se + próximo vídeo, nos últimos 15–20 s |
| Anúncios no meio | só se o vídeo tem 8 min ou mais; marcar nas pausas naturais |
| Data e hora | … no fuso do público e … no fuso do dono (calculado por código) |
| Short de chamada | arquivo … , "Vídeo relacionado" = este vídeo, publicar em … |
| Legenda | arquivo .srt revisado (sobe melhor que a automática) |
```

Para converter o horário, use código, porque os fusos mudam no horário de verão:

```bash
uv run python -c "from datetime import datetime; from zoneinfo import ZoneInfo as Z; t=datetime(2026,11,5,12,tzinfo=Z('America/New_York')); print(t.astimezone(Z('America/Sao_Paulo')))"
```

O horário é uma **hipótese** enquanto o canal não tiver dados. Depois, vale a aba "Quando seus espectadores estão no YouTube" do Studio.

## Short de chamada

Um Short por vídeo longo, de **61 a 90 s**. Passar de 1 min é de propósito: o TikTok só paga pelo programa Creator Rewards vídeos com mais de 1 min, e Shorts e Reels aceitam até 3 min. O mesmo arquivo serve para YouTube Shorts, Instagram Reels e TikTok.

- **O que entra:** abertura + crença errada + promessa + a primeira prova (tempos 1, 2 e o começo do 3 do explicador), terminando num laço aberto que só o vídeo longo fecha. Em outros formatos: o gancho e o primeiro terço da história, cortando antes da virada.
- **Segurar mais de um minuto:** algo muda a cada 2 a 3 s, legenda grande o tempo todo e uma mini-revelação perto dos 45 a 60 s, para quem chegou ali ter motivo de ficar até o fim.
- **Vertical de verdade.** Como vai para três redes, monte o Short em 9:16 a partir das mesmas imagens, inserts e narração (no HyperFrames ou Remotion: a cena ocupa a tela, os inserts são refeitos para o vertical), em vez de colar o vídeo horizontal sobre um fundo desfocado. O fundo desfocado fica como plano B rápido. `<fim>` é o ponto do laço aberto, tirado da transcrição:

  ```bash
  ffmpeg -y -i final/<tema>-videos.mp4 -t <fim> -vf "split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:3[bg];[b]scale=1080:-2[fg];[bg][fg]overlay=0:(H-h)/2" -c:a aac rascunhos/<tema>-reels-v1.mp4
  ```

- **Música só com licença liberada** (biblioteca do estúdio, Biblioteca de Áudio do YouTube ou trilha própria). No YouTube, Short com mais de 1 min e qualquer reivindicação do Content ID é bloqueado no mundo todo. Não use música famosa nem música da biblioteca de uma rede dentro do arquivo.
- **Um arquivo limpo para cada rede.** Exporte do estúdio, sem marca d'água, e suba o mesmo arquivo em cada plataforma. Nunca baixe do TikTok para subir no Instagram: o Instagram já disse que mostra menos Reels com marca d'água de outro app.
- **Rótulo de IA em cada rede**, pelas regras de cada uma ([politicas-ia.md](politicas-ia.md)).
- **Chamada para o vídeo longo:** no YouTube, "Vídeo relacionado" = o vídeo longo e título = a pergunta do vídeo + `#shorts`. No Instagram e no TikTok o link não é clicável no vídeo: chamada falada ou na tela ("o vídeo completo está no YouTube") e link na bio. Legenda e hashtags de cada rede pela `copy-redes`.
- O Short é uma peça própria (`uv run scripts/peca.py nova reels "tema"`), com a área segura do 9:16 conferida (regras.md) e as datas de cada rede no `calendario.md` da marca.

## Checklist antes de entregar

- [ ] Vídeo final aprovado pelo dono (data e palavras dele no `README.md` da peça).
- [ ] Checklist de originalidade ([politicas-ia.md](politicas-ia.md#checklist-de-originalidade-antes-de-publicar)) passado.
- [ ] Miniatura legível no tamanho do celular, fiel ao vídeo, sem repetir o título, texto revisado.
- [ ] Títulos com até 60 caracteres (contados por código).
- [ ] Capítulos com os tempos reais do corte final.
- [ ] Fontes e créditos na descrição; licenças de música, efeitos e imagens anotadas. O checklist não garante Content ID nem monetização: o que não tem prova de licença fica marcado como pendente.
- [ ] Rótulo de IA decidido e anotado.
- [ ] Short de chamada pronto: 61 a 90 s, montado na vertical, área segura conferida, música com licença liberada, arquivo sem marca d'água.
- [ ] Linha da peça atualizada no `calendario.md` da marca.
