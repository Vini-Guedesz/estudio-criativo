// Otimiza os SVGs do logo da marca (SVGO).
// Uso (da raiz):  npm run svg --prefix scripts/design -- [--marca nome]
// Lê 04-marcas/<marca>/identidade/logo/*.svg e salva em identidade/logo/otimizado/.
import { optimize } from 'svgo';
import { readdirSync, readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';
import { argumentos, marca, rel } from './estudio.mjs';

const logo = join(marca(argumentos().opcoes.marca), 'identidade', 'logo');
const saida = join(logo, 'otimizado');
const svgs = readdirSync(logo).filter((f) => f.toLowerCase().endsWith('.svg'));
if (!svgs.length) { console.log('Nenhum SVG em', rel(logo)); process.exit(0); }
mkdirSync(saida, { recursive: true });
for (const f of svgs) {
  const { data } = optimize(readFileSync(join(logo, f), 'utf8'), { multipass: true });
  writeFileSync(join(saida, f), data);
  console.log('Otimizado:', rel(join(saida, f)));
}
