# Criando e escrevendo em um arquivo
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Este é a primeira linha do arquivo.\n")
    arquivo.write("Está é a segunda linha.")


with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)