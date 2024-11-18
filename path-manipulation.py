import os

#Verifica diretorio atual
arquivos = os.listdir(".")
print (arquivos)

#Verifica se um arquivo existe

if os.path.exists("exemplo.txt"):
    print("O arquivo existe")
else:
    print("O arquivo não foi encontrado.")
    
    