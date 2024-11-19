import os
from pathlib import Path

diretorio_atual= Path(".")

for arquivo in diretorio_atual.iterdir():
    print(arquivo)

arquivo = Path("exemplo.txt")
arquivo.rename("exemplo_renomeado.txt")