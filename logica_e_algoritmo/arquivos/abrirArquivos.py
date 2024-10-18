"""
r - read 
a - append - inserir registro
w - write - escrever
x - criar arquivo
rw - leitura e escrita
"""

#open("CAMINHO", modo de abertura)
arquivo = open("texto.txt","r")

#retorna se o arquivo pode ser lido
print(arquivo.readable())
#imprimir os dados do arquivo chamado arquivo
print(arquivo.read())