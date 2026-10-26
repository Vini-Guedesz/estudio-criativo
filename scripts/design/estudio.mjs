// Caminhos do estúdio para os scripts Node: as mesmas regras do scripts/_estudio.py (mudou lá? mude aqui).
// Tudo de uma marca fica em 04-marcas/<marca>/; cada peça em 04-marcas/<marca>/<tipo>/AAAA-MM-DD-tema/.
import { existsSync, readdirSync, statSync, mkdirSync } from 'node:fs';
import { dirname, join, resolve, relative, basename } from 'node:path';
import { fileURLToPath } from 'node:url';

export const AQUI = dirname(fileURLToPath(import.meta.url));
export const RAIZ = resolve(AQUI, '..', '..');
export const MARCAS = join(RAIZ, '04-marcas');
// Pasta de onde o comando foi chamado (o npm muda para scripts/design; INIT_CWD guarda a original).
const ORIGEM = process.env.INIT_CWD || process.cwd();

export const TIPOS = { reels: 'reels', videos: 'video', stories: 'story', posts: 'post', carrosseis: 'carrossel' };

// 'Lançamento da Coleção!' → 'lancamento-da-colecao' (igual ao slug() do Python)
export const slug = (t) => String(t).normalize('NFKD').replace(/\p{M}/gu, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');

export const rel = (p) => relative(RAIZ, p).replaceAll('\\', '/');
const ehPasta = (p) => existsSync(p) && statSync(p).isDirectory();

// Lê "--chave valor" e devolve { opcoes, resto } (o resto são os textos soltos, em ordem).
export function argumentos(lista = process.argv.slice(2)) {
  const opcoes = {}, resto = [];
  for (let i = 0; i < lista.length; i++) {
    if (lista[i].startsWith('--')) opcoes[lista[i].slice(2)] = lista[i + 1]?.startsWith('--') ? true : lista[++i] ?? true;
    else resto.push(lista[i]);
  }
  return { opcoes, resto };
}

export function marcas() {
  if (!ehPasta(MARCAS)) return [];
  return readdirSync(MARCAS).filter((n) => !n.startsWith('_') && !n.startsWith('.') && ehPasta(join(MARCAS, n))).sort();
}

// Pasta da marca. Sem nome, usa a única marca que existir.
export function marca(nome) {
  if (nome) {
    const p = join(MARCAS, slug(nome));
    if (!ehPasta(p)) sair(`a marca '${nome}' não existe em 04-marcas/. Crie com: uv run scripts/peca.py marca "${nome}"`);
    return p;
  }
  const todas = marcas();
  if (todas.length === 1) return join(MARCAS, todas[0]);
  if (!todas.length) sair('ainda não há marca. Crie com: uv run scripts/peca.py marca "Nome da marca"');
  sair(`há mais de uma marca; diga qual com --marca (${todas.join(', ')})`);
}

// Pasta da peça pelo caminho ou só pelo nome da pasta (ex.: 2026-10-25-lancamento).
export function peca(caminho) {
  if (!caminho || caminho === true) sair('diga a peça com --peca (crie com: uv run scripts/peca.py nova post "tema")');
  for (const c of [resolve(ORIGEM, caminho), resolve(RAIZ, caminho)]) if (ehPasta(c)) return c;
  const achadas = marcas().flatMap((m) => Object.keys(TIPOS).map((t) => join(MARCAS, m, t, basename(caminho)))).filter(ehPasta);
  if (achadas.length === 1) return achadas[0];
  sair(`não achei a peça '${caminho}'${achadas.length ? ` (há ${achadas.length} com esse nome)` : ''}`);
}

// Marca dona de uma peça: 04-marcas/<marca>/<tipo>/<peça> → 04-marcas/<marca>
export const marcaDaPeca = (pastaPeca) => resolve(pastaPeca, '..', '..');

export const tokensDaMarca = (pastaMarca) => join(pastaMarca, 'identidade', 'design-tokens', 'marca.json');

// Próximo rascunho: rascunhos/<tema>-<tipo>-v<N>[-<parte>].<ext>
export function rascunho(pastaPeca, ext, { parte, mesmaVersao } = {}) {
  const tema = basename(pastaPeca).replace(/^\d{4}-\d{2}-\d{2}-/, '');
  const suf = TIPOS[basename(dirname(pastaPeca))] ?? basename(dirname(pastaPeca));
  const pasta = join(pastaPeca, 'rascunhos');
  mkdirSync(pasta, { recursive: true });
  const prefixo = `${tema}-${suf}-v`;
  const versoes = readdirSync(pasta).filter((f) => f.startsWith(prefixo)).map((f) => parseInt(f.slice(prefixo.length), 10)).filter((n) => !isNaN(n));
  let n = Math.max(0, ...versoes);
  n = mesmaVersao ? Math.max(n, 1) : n + 1;
  const fim = parte ? `-${String(parte).padStart(2, '0')}` : '';
  return join(pasta, `${prefixo}${n}${fim}.${ext}`);
}

export function sair(msg) {
  console.error(`erro: ${msg}`);
  process.exit(1);
}
