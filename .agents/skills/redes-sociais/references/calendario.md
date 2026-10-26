# Calendário editorial e reaproveitamento

> Data: 2026-10-25 · Tipo: guia · Status: vigente

**Resumo:** como montar o calendário de uma marca (pilares, ritmo, mix de formatos, ideias) e como transformar uma peça mãe em várias. O calendário vive em `04-marcas/<marca>/calendario.md`, criado a partir do modelo da marca.

## 1. Pilares

De 3 a 5 temas fixos, tirados da seção 7 do briefing e da `plataforma.md`. Cada pilar ganha uma fatia do calendário e um objetivo.

| Pilar | Fatia | Objetivo | Exemplo (confeitaria) |
|---|---|---|---|
| Ensinar | 40% | alcance e salvamento | técnicas, erros comuns, receitas simples |
| Bastidor | 20% | confiança e proximidade | produção, rotina, quem faz |
| Prova | 20% | desejo | encomendas entregues, cliente real falando (com autorização) |
| Oferta | 20% | venda | cardápio, agenda aberta, datas comemorativas |

A fatia de oferta raramente passa de 20% a 30%. Conta que só vende perde quem segue.

**Perene e tendência:** pelo menos 70% do calendário é conteúdo que continua útil depois (perene). Até 30% acompanha tendência (áudio, formato, assunto do momento), sempre dentro de um pilar.

## 2. Ritmo

Pergunte ao dono quanto tempo ele tem por semana e quanto custa cada formato para ele. Ritmos de partida:

| Perfil | Ritmo semanal de partida |
|---|---|
| Dono sozinho, começando | 2 Reels + 1 carrossel + stories em 3 dias |
| Dono com rotina de produção | 3 a 4 Reels + 2 carrosséis + stories todo dia útil |
| Marca com equipe | defina pelo histórico de `resultados.md` |

Constância é o que importa. Mude o ritmo só depois de um mês cumprido.

**Dia e hora:** comece pelos horários em que o público da conta está online (Insights do Instagram, Analytics do TikTok, YouTube Studio). Sem dado ainda, teste horários diferentes nas primeiras semanas e registre no `resultados.md`.

## 3. Ideias

Fontes de pauta, em ordem de valor:

1. **Perguntas do público:** comentários, mensagens, caixa de pergunta dos stories. Cada pergunta repetida é uma peça.
2. **O que já funcionou:** os melhores do `resultados.md` ganham continuação, outro ângulo ou outro formato.
3. **Referências do nicho:** `03-referencias/` e perfis parecidos. Desmonte o que funcionou ([metricas.md](metricas.md#desmontar-um-conteúdo-que-funcionou)) e adapte à marca, sem copiar.
4. **Datas:** lançamentos da marca, datas que importam ao público (Dia das Mães para uma confeitaria, volta às aulas para papelaria). Planeje com 2 a 4 semanas de antecedência.
5. **Tendências** que cabem num pilar.

Para cada ideia, anote: pilar, formato, gancho provisório, objetivo e CTA.

## 4. A tabela

No `calendario.md` da marca, uma linha por peça:

| Data | Plataforma | Formato | Pilar | Tema / gancho provisório | Objetivo · CTA | Status | Peça |
|---|---|---|---|---|---|---|---|
| 2026-11-03 | Instagram, TikTok | Reels | Ensinar | "Por que seu brigadeiro açucara" | alcance · mandar para alguém | ideia | |
| 2026-11-05 | Instagram | Carrossel | Ensinar | 5 erros na ganache | salvar | produção | `carrosseis/2026-11-05-erros-ganache` |

**Status:** `ideia` → `aprovada` → `produção` → `revisão` → `pronta` (em `final/`) → `publicada` → `medida` (números no `resultados.md`).

Mostre o calendário ao dono antes de abrir as peças. Aprovado, abra cada peça com `uv run scripts/peca.py nova <tipo> "tema" --data <data>` e preencha a coluna "Peça".

## Reaproveitar

Uma **peça mãe** (vídeo longo, live, aula, Reels que foi muito bem) rende várias peças menores. Cada uma vira uma pasta nova, com a peça mãe citada no README.

```
videos/2026-11-10-como-precificar-bolos/          ← peça mãe
reels/2026-11-12-erro-de-precificacao/             ← corte 1 (gancho novo)
reels/2026-11-15-custo-escondido/                  ← corte 2
carrosseis/2026-11-14-formula-de-preco/            ← os passos do vídeo em telas
stories/2026-11-11-bastidor-precificacao/          ← chamada para o vídeo
```

Passo a passo:

1. **Transcreva** a peça mãe: `uv run scripts/video/make_captions.py <video> legendas.json` (gera também o `.srt` com os tempos).
2. **Marque de 3 a 7 trechos** que funcionam sozinhos: uma dica completa, uma opinião forte, uma história curta, um antes e depois. Anote o tempo de início e fim no README da peça mãe.
3. **Para cada trecho, decida o formato:** fala forte vira corte vertical, lista vira carrossel, bastidor vira stories.
4. **Gancho novo para cada corte.** O começo do trecho raramente é um bom gancho. Escreva um (texto na tela + primeira frase) com a `copy-redes`.
5. **Abra as peças** e produza. Os assets da peça mãe são copiados para a pasta da peça nova (cada peça é autossuficiente).
6. **Espalhe no calendário.** Os cortes não saem todos no mesmo dia. Intercale com outros pilares.

Cada peça reaproveitada tem gancho, formato e CTA próprios para a plataforma. Repostar o mesmo arquivo em todo lugar não conta.
