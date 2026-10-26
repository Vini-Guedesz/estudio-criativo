"""Remove o fundo de uma foto (avatar, produto, rosto). Gera PNG transparente.
Uso: uv run scripts/design/sem_fundo.py foto.jpg [modelo]
Modelos: isnet-general-use (padrão, ~170 MB, bom para tudo) · u2net_human_seg (pessoas)
         · birefnet-general (~1 GB, melhor recorte de cabelo e bordas, mais lento)
O modelo baixa só na primeira vez que é usado."""
import sys
from pathlib import Path
from PIL import Image
from rembg import new_session, remove

entrada = Path(sys.argv[1])
modelo = sys.argv[2] if len(sys.argv) > 2 else "isnet-general-use"
saida = entrada.with_name(entrada.stem + "-sem-fundo.png")
remove(Image.open(entrada), session=new_session(modelo)).save(saida)
print(f"Salvo em {saida} (modelo {modelo})")
