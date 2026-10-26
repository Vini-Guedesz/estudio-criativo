// Exporta as cores e fontes da marca para CSS e JSON (Style Dictionary), usados por posts e vídeos.
// Uso (da raiz):  npm run tokens --prefix scripts/design -- [--marca nome]
// Lê:  04-marcas/<marca>/identidade/design-tokens/marca.json
// Sai: 04-marcas/<marca>/identidade/design-tokens/saida/marca.css e marca.json
import StyleDictionary from 'style-dictionary';
import { join } from 'node:path';
import { argumentos, marca, tokensDaMarca, rel } from './estudio.mjs';

const pastaMarca = marca(argumentos().opcoes.marca);
const saida = join(pastaMarca, 'identidade', 'design-tokens', 'saida') + '/';
const sd = new StyleDictionary({
  source: [tokensDaMarca(pastaMarca)],
  log: { verbosity: 'silent' },
  platforms: {
    css: { transformGroup: 'css', buildPath: saida, files: [{ destination: 'marca.css', format: 'css/variables' }] },
    json: { transformGroup: 'js', buildPath: saida, files: [{ destination: 'marca.json', format: 'json/flat' }] },
  },
});
await sd.buildAllPlatforms();
console.log('Tokens salvos em', rel(saida));
