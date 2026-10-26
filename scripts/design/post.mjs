// Gera um post 1080x1350 (feed e carrossel) em PNG com a identidade da marca, direto em rascunhos/ da peça.
// Uso (da raiz):  npm run post --prefix scripts/design -- --peca <peça> "Título" "texto de apoio" [opções]
//   --peca <peça>       pasta da peça (crie antes: uv run scripts/peca.py nova post "tema"); aceita só o nome da pasta
//   --layout <nome>     capa (padrão) · conteudo · cta
//   --estilo <ficha>    ficha de 03-referencias/estilos (padrão: o "estilo" do marca.json, senão clean-tech)
//   --numero <n>        número grande do layout conteudo (ex.: 1, 2, 3)
//   --rotulo <texto>    etiqueta curta acima do título (ex.: "Como funciona")
//   --parte N           tela N de um carrossel (a partir da 2ª tela, some --mesma-versao)
// Lê da marca: cores e fontes (identidade/design-tokens/marca.json) e o logo (identidade/logo/).
// As cores de texto são escolhidas pelo contraste (texto pequeno >= 4,5; título >= 3), nunca só pelo nome do token.
// Sai em: 04-marcas/<marca>/<posts|carrosseis>/<peça>/rascunhos/<tema>-<tipo>-v<N>.png
import satori from 'satori';
import { Resvg } from '@resvg/resvg-js';
import { wcagContrast } from 'culori';
import { readFileSync, writeFileSync, existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';
import { AQUI, argumentos, peca, marcaDaPeca, tokensDaMarca, rascunho, rel, slug, sair } from './estudio.mjs';

const { opcoes, resto } = argumentos();
const pastaPeca = peca(opcoes.peca);
const pastaMarca = marcaDaPeca(pastaPeca);
const marca = JSON.parse(readFileSync(tokensDaMarca(pastaMarca), 'utf8'));
const [titulo = 'Título do post', apoio = ''] = resto;
const layout = opcoes.layout || 'capa';
if (!['capa', 'conteudo', 'cta'].includes(layout)) sair(`layout '${layout}' não existe. Use: capa, conteudo, cta`);

// ---------- cores: tokens da marca + escolha por contraste ----------
const tok = (k) => marca.cor?.[k]?.value;
const C = {
  primaria: tok('primaria') || '#111111',
  primariaEscura: tok('primaria-escura') || tok('primaria') || '#111111',
  secundaria: tok('secundaria') || tok('primaria') || '#111111',
  secundariaTexto: tok('secundaria-texto'),
  fundo: tok('fundo') || '#FFFFFF',
  superficie: tok('superficie') || tok('fundo') || '#F2F2F2',
  texto: tok('texto') || '#111111',
  textoSec: tok('texto-secundario') || tok('texto') || '#444444',
};
const contraste = (a, b) => wcagContrast(a, b);
// primeira cor da lista que passa no contraste mínimo sobre o fundo; se nenhuma passar, a de maior contraste
function textoSobre(fundo, candidatas, minimo = 4.5) {
  const validas = candidatas.filter(Boolean);
  return validas.find((c) => contraste(c, fundo) >= minimo)
    || validas.sort((a, b) => contraste(b, fundo) - contraste(a, fundo))[0];
}

// ---------- estilo: a ficha vira um dos modelos de post ----------
const MODELO_DO_ESTILO = {
  'clean-tech': 'limpo', glassmorfismo: 'limpo', 'flat-ilustrado': 'limpo', '3d-clay': 'limpo', doodle: 'limpo', colagem: 'limpo',
  neobrutalismo: 'bloco', memphis: 'bloco', 'pixel-art': 'bloco',
  'minimalismo-suico': 'grade', 'tipografia-cinetica': 'grade', risografia: 'grade',
  'luxo-escuro': 'escuro', synthwave: 'escuro', y2k: 'escuro', 'vhs-lofi': 'escuro',
};
const estilo = slug(opcoes.estilo || marca.estilo?.value || 'clean-tech');
const modelo = MODELO_DO_ESTILO[estilo];
if (!modelo) sair(`estilo '${estilo}' não tem modelo de post. Use um destes: ${Object.keys(MODELO_DO_ESTILO).join(', ')}`);

const escuro = modelo === 'escuro';
const bg = escuro ? (contraste(C.primariaEscura, '#FFFFFF') >= 7 ? C.primariaEscura : C.texto) : (modelo === 'bloco' ? C.superficie : C.fundo);
const corTitulo = textoSobre(bg, escuro ? ['#FFFFFF', C.fundo] : [C.primaria, C.texto], 3);
const corTexto = textoSobre(bg, escuro ? [C.fundo, '#FFFFFF'] : [C.textoSec, C.texto]);
const corDestaque = textoSobre(bg, [C.secundariaTexto, C.secundaria, C.primaria, corTitulo]);
const corForma = C.secundaria; // forma decorativa: não precisa de contraste de texto
const corSobreForma = textoSobre(corForma, [C.texto, '#FFFFFF', C.fundo]);

// ---------- fontes da marca (pacotes @fontsource em scripts/design) ----------
function carregaFonte(familia, peso) {
  const s = slug(familia);
  const arq = join(AQUI, 'node_modules', '@fontsource', s, 'files', `${s}-latin-${peso}-normal.woff`);
  return existsSync(arq) ? readFileSync(arq) : null;
}
const famTitulo = marca.fonte?.titulo?.value || 'Inter';
const famTexto = marca.fonte?.texto?.value || famTitulo;
const fontes = [];
for (const [fam, pesos, nome] of [[famTitulo, [800, 700], 'Titulo'], [famTexto, [400, 600], 'Texto']]) {
  for (const p of pesos) {
    const dado = carregaFonte(fam, p) || carregaFonte('Inter', p >= 700 ? 800 : 400);
    if (!carregaFonte(fam, p) && p === pesos[0]) console.log(`aviso: fonte "${fam}" (peso ${p}) não instalada; usando Inter. Instale: npm install @fontsource/${slug(fam)} --prefix scripts/design`);
    fontes.push({ name: nome, data: dado, weight: p, style: 'normal' });
  }
}

// ---------- logo da marca ----------
function logo(fundo) {
  const pasta = join(pastaMarca, 'identidade', 'logo');
  if (!existsSync(pasta)) return null;
  const svgs = readdirSync(pasta).filter((f) => f.toLowerCase().endsWith('.svg'));
  const claro = contraste(fundo, '#FFFFFF') < 3;
  const pref = claro
    ? [/horizontal\.svg$/, /horizontal(?!.*(negativo|branco))/, /simbolo(?!.*(negativo|branco))/]
    : [/horizontal-negativo/, /mono-branco/, /negativo/];
  for (const re of pref) {
    const f = svgs.find((n) => re.test(n));
    if (f) {
      const svg = readFileSync(join(pasta, f), 'utf8');
      const vb = svg.match(/viewBox="[\d.\s-]*?([\d.]+)\s+([\d.]+)"/);
      const proporcao = vb ? parseFloat(vb[1]) / parseFloat(vb[2]) : 1;
      return { src: `data:image/svg+xml;base64,${Buffer.from(svg).toString('base64')}`, proporcao, arquivo: f };
    }
  }
  return null;
}

// ---------- montagem ----------
const h = (type, style, children) => ({ type, props: { style: { display: 'flex', ...style }, children } });
const img = (src, width, height) => ({ type: 'img', props: { src, width, height } });
const L = logo(bg);
if (!L) console.log('aviso: sem logo em identidade/logo/ (horizontal ou símbolo); o post sai sem logo.');
const ALTURA_LOGO = 64;
const blocoLogo = L ? img(L.src, Math.round(ALTURA_LOGO * L.proporcao), ALTURA_LOGO) : h('div', {}, []);

const raio = { limpo: 28, bloco: 0, grade: 0, escuro: 4 }[modelo];
const caixaBloco = modelo === 'bloco' ? { border: `5px solid ${C.texto}`, boxShadow: `12px 12px 0 ${C.texto}`, background: C.fundo, padding: '48px 52px' } : {};
const rotulo = opcoes.rotulo
  ? h('div', { alignSelf: 'flex-start', background: corForma, color: corSobreForma, fontFamily: 'Texto', fontWeight: 600, fontSize: 30, padding: '10px 26px', borderRadius: raio ? 999 : 0, marginBottom: 34 }, opcoes.rotulo)
  : null;
const tamTitulo = layout === 'capa' ? (titulo.length > 48 ? 84 : 100) : (titulo.length > 60 ? 64 : 76);
// no modelo bloco o texto fica dentro da caixa (borda 5 + respiro 52 de cada lado)
const larguraTexto = modelo === 'bloco' ? 900 - 2 * (52 + 5) : 900;
const blocoTitulo = h('div', { fontFamily: 'Titulo', fontWeight: 800, fontSize: tamTitulo, lineHeight: 1.04, letterSpacing: -1.5, color: corTitulo, width: larguraTexto }, titulo);
const blocoApoio = apoio ? h('div', { fontFamily: 'Texto', fontWeight: 400, fontSize: 38, lineHeight: 1.35, color: corTexto, marginTop: 30, width: larguraTexto }, apoio) : null;
const numero = layout === 'conteudo' && opcoes.numero
  ? h('div', { fontFamily: 'Titulo', fontWeight: 800, fontSize: 220, lineHeight: 0.9, letterSpacing: -8, color: corDestaque, marginBottom: 30 }, String(opcoes.numero))
  : null;
// a régua usa a primária, mas no fundo escuro troca pela cor do título (a primária some sobre azul escuro)
const corRegua = contraste(C.primaria, bg) >= 3 ? C.primaria : corTitulo;
const regua = h('div', { width: '100%', height: modelo === 'grade' ? 4 : 14, borderRadius: modelo === 'limpo' ? 8 : 0, background: modelo === 'grade' ? corTitulo : `linear-gradient(90deg, ${corRegua} 0%, ${corRegua} 70%, ${corForma} 70%, ${corForma} 100%)` }, []);

const miolo = [rotulo, numero, blocoTitulo, blocoApoio].filter(Boolean);
const centro = h('div', { flexDirection: 'column', ...caixaBloco }, miolo);
let filhos;
if (layout === 'cta') {
  const botao = h('div', { alignSelf: 'flex-start', marginTop: 44, background: escuro ? corForma : C.primaria, color: escuro ? corSobreForma : textoSobre(C.primaria, ['#FFFFFF', C.fundo]), fontFamily: 'Texto', fontWeight: 600, fontSize: 36, padding: '24px 48px', borderRadius: raio ? 999 : 0 }, opcoes.botao || 'Fale com a gente');
  filhos = [h('div', {}, []), h('div', { flexDirection: 'column' }, [centro, botao]), h('div', { flexDirection: 'column', gap: 40 }, [regua, blocoLogo])];
} else {
  filhos = [blocoLogo, centro, regua];
}

const arte = h('div', { width: 1080, height: 1350, flexDirection: 'column', justifyContent: 'space-between', padding: 90, boxSizing: 'border-box', background: bg }, filhos);
const svg = await satori(arte, { width: 1080, height: 1350, fonts: fontes });
const png = new Resvg(svg, { fitTo: { mode: 'width', value: 1080 } }).render().asPng();
const arquivo = rascunho(pastaPeca, 'png', { parte: opcoes.parte, mesmaVersao: Boolean(opcoes['mesma-versao']) });
writeFileSync(arquivo, png);
console.log(`Post salvo em ${rel(arquivo)}  (estilo ${estilo} → modelo ${modelo}, layout ${layout}${L ? `, logo ${L.arquivo}` : ''})`);
console.log('Aprovado? uv run scripts/peca.py aprovar', rel(arquivo));
