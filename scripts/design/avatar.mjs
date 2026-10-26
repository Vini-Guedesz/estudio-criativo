// Gera avatares (SVG) para a marca, em 04-marcas/<marca>/identidade/avatar/.
// Uso (da raiz):  npm run avatar --prefix scripts/design -- "semente" estilo [--marca nome]
// Estilos: notionists, lorelei, avataaars, shapes, glass, thumbs ... (veja dicebear.com/styles)
import { createAvatar } from '@dicebear/core';
import * as estilos from '@dicebear/collection';
import { writeFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';
import { argumentos, marca, rel } from './estudio.mjs';

const { opcoes, resto } = argumentos();
const [semente = 'minha-marca', estilo = 'notionists'] = resto;
if (!estilos[estilo]) { console.log('Estilo não existe. Opções:', Object.keys(estilos).join(', ')); process.exit(1); }
const pasta = join(marca(opcoes.marca), 'identidade', 'avatar');
const svg = createAvatar(estilos[estilo], { seed: semente, size: 512 }).toString();
mkdirSync(pasta, { recursive: true });
const arquivo = join(pasta, `${estilo}-${semente}.svg`);
writeFileSync(arquivo, svg);
console.log('Avatar salvo em', rel(arquivo));
