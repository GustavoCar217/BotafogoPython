alunos =["simone","vanessa","fernando","ricardo"] #lista
            #0      1           2           3

print(alunos[0])
print(alunos)
#modificando valores
alunos[0] = "simone neves"
print(alunos)

#adicionar valor em lista
alunos.extend(["gustavo"])
print(alunos)
#adicionar um registro em lista 
alunos.append("aurelio")
print(alunos)

alunos.insert(0,"maria eduarda")
print(alunos)

alunos.remove("simone neves")
print(alunos)
#alunos.remove (["vanessa"]) #não colocar colchete
print(alunos)
# R E M O V E no final da lista 
alunos.pop()
print(alunos)
alunos.pop()
print(alunos)
# Apagar o conteúdo de uma lista 
#alunos.clear()
print(alunos)
alunos.sort()
print(alunos)