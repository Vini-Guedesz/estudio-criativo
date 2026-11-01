# Crescimento de canal dark

> Data: 2026-11-01 · Tipo: guia · Status: vigente

**Resumo:** como o YouTube distribui um vídeo, como diagnosticar um canal que não cresce (um gargalo por vez), como estudar o que funciona em outros canais sem copiar, e como tirar cortes de um vídeo longo. Os números de cada vídeo vão para o `resultados.md` da marca pela skill `redes-sociais`. Os números de mercado daqui são de terceiros: servem de pista até o canal ter os próprios.

## Como o YouTube distribui

- **Não existe um algoritmo só.** Busca, página inicial, sugeridos e Shorts são sistemas separados. Um vídeo pode ir bem num e mal no outro. Primeiro passo de qualquer análise: qual fonte de tráfego domina (Studio > Alcance > Fontes de tráfego).
- **Teste em ondas.** O vídeo é mostrado a um grupo pequeno (inscritos e habituais), depois a um público parecido, depois a temas vizinhos, depois à página inicial ampla. Cada onda depende de como foi a anterior. Por isso as primeiras 24 a 72 h pesam, e um vídeo pode voltar a subir semanas depois.
- **O que conta, em ordem aproximada:** satisfação (pesquisas pós-vídeo, compartilhamentos, voltar ao canal, "não tenho interesse"); taxa de clique entre quem não é inscrito; quanto e como as pessoas assistem (os primeiros 30 s decidem); se a pessoa continua no YouTube depois (séries, playlists, tela final); relevância (título, descrição e as palavras faladas, porque o YouTube lê a transcrição).
- **"Algoritmo" é o público.** Ele mede o comportamento das pessoas. Não existe truque: entender por que clicam, por que saem e por que compartilham.
- **Inscritos pesam pouco.** Canal pequeno pode explodir se o vídeo for bem no teste.
- **Shorts são outro mundo:** quase não importa o clique; importa quantos assistem em vez de deslizar, quantos assistem até o fim e quantos repetem. Um Short pode decolar até uns 4 dias depois. Funciona como porta de entrada para o vídeo longo.
- **Clique enganoso é punido.** O YouTube compara título e miniatura com o conteúdo, e um clique que não vira visualização satisfeita derruba o vídeo.

## Diagnóstico: um gargalo por vez

Quando o dono pergunta "por que não decola" ou pede uma auditoria:

1. **Medir antes de opinar.** Peça de uma vez os números do Studio dos últimos 28 dias (impressões, taxa de clique, duração média, retenção aos 30 s, fontes de tráfego, países, horários) por print (vai para `00-entrada/`) ou digitados. Para canal público, títulos, datas e durações podem ser lidos da página do canal. Sem número, diga o que ficou sem dado; nunca invente.
2. **Achar o gargalo**, só um:

| Sintoma | Gargalo | Onde mexer |
|---|---|---|
| Poucas impressões | tema e embalagem não atraem o teste | tema (teste do espelho), título, consistência do canal |
| Muitas impressões, clique baixo | miniatura e título | [visual.md · miniatura](visual.md#miniatura), 5 títulos novos, teste A/B |
| Queda forte antes de 30 s | gancho | refazer os 30 s ([roteiro.md · retenção](roteiro.md#retenção)) |
| Queda lenta e contínua | ritmo e duração | cortar enchimento, mais trocas, vídeo mais curto |
| Vale no meio do vídeo | trecho fraco | reordenar, insert, laço aberto |
| Vídeos isolados, sem segunda visualização | sessão | séries, playlists, tela final, Short de chamada |
| Público do país errado | sinais do conteúdo | idioma, voz, referências, horário (nunca VPN ou troca de país) |

3. **Consistência primeiro.** Um formato, um estilo, uma duração, um molde de miniatura. Canal que muda a cada vídeo confunde o teste.
4. **Entregar `auditoria.md`** na pasta `04-marcas/<canal>/` (resumo no chat): diagnóstico com os números, o que o YouTube espera deste canal (3 a 5 pontos), otimizações (3 títulos, 2 miniaturas, gancho reescrito do pior vídeo), plano de 30 dias (no máximo 5 ações por semana, cada uma com o número que vai mostrar se funcionou). Nunca prometer views ou prazo.

## Estudar o que funciona (sem copiar)

- **Vídeos fora da curva.** Procure, no nicho, vídeos de canais pequenos com 10 vezes ou mais as views normais do canal. Esses mostram tema e embalagem que o público quer, não o tamanho do canal.
- **Desmonte, não refaça.** Cada referência vira análise em `03-referencias/analises/` (método da `redes-sociais`, "desmontar um conteúdo que funcionou"): tema, gancho, estrutura, duração, miniatura, título, ritmo. A gente leva a mecânica; texto, imagem e personagem são do outro canal.
- **Onda de formato.** Quando vários canais novos de um nicho fazem centenas de milhares de views em poucas semanas, há demanda. Dá para entrar rápido com a embalagem do grupo, mas com o canal se diferenciando pelo tema e pelo personagem desde cedo. Copiar até ficar intercambiável é o que a política pune.
- **Quando um vídeo decola:** uma continuação (mesmo tema, outro ângulo) em 24 a 48 h, ligada ao vídeo original.
- **Os 100 primeiros vídeos são treino.** Melhore uma coisa por vídeo (gancho, miniatura, ritmo) e anote no `06-metodo/aprendizados.md`. Não espere resultado estável antes de dezenas de vídeos.

## Cadência

- **Constância vale mais que volume.** 4 por mês todo mês ganha de 12 num mês e nada no outro.
- O YouTube manda no máximo 3 notificações por canal a cada 24 h; mais uploads que isso não avisam os inscritos.
- A cadência certa é a que a produção aguenta **sem baixar a qualidade e sem repetir**. Produção em massa é justamente o que a política de conteúdo inautêntico descreve.
- Pausa não é punida, segundo o YouTube.

## Cortes do vídeo longo

Para tirar Shorts de um vídeo já pronto (ou de uma gravação longa do dono):

1. Transcreva com `uv run scripts/video/make_captions.py` (tempo de cada palavra).
2. Liste 8 a 12 trechos de 15 a 55 s e dê nota de 0 a 100, com estes pesos:

| Critério | Peso | O que procurar |
|---|---|---|
| Força do gancho | 30% | afirmação forte, curiosidade, promessa, quebra de padrão |
| Faz sentido sozinho | 25% | dá para entender sem o resto do vídeo |
| Emoção | 20% | surpresa, opinião forte, humor |
| Densidade | 15% | fatos e ideias por segundo |
| Fecho | 10% | uma conclusão, revelação ou frase de efeito |

3. Mostre a tabela (tempo, duração, nota, gancho sugerido para os 3 primeiros segundos, por que funciona) e o dono escolhe.
4. Ajuste início e fim para nunca cortar no meio da palavra (pausas da transcrição).
5. Cada corte vira peça `reels`, com legenda grande e área segura conferida. Cortes do mesmo vídeo publicados em dias diferentes, cada um com o vídeo longo como "Vídeo relacionado".
