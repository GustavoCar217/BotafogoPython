#set -> desordenado, não aceita repetições
#ao executar o resultado é sempre diferente
# não consigo buscar por índice

frutas = {"maças","laranja","banana","pera","uva","maças","maças","maças",} # não repete
print(frutas)
print("-------------")
#adicionar algo ao set
frutas.add("melão")
print(frutas)
print("-------------")
#remover algo ao set
frutas.remove("uva")
print(frutas)
print("**************")
frutas.pop() # remove o ultimo 
print(frutas)
print("====================")
# pop remove o item da lista ou set, porém como
# o set não é ordenado, nunca sabemos quem é o ultimo item da lista


conjunto1 = {"maça","uva","ameixa",} #string
conjunto2 = {100,200,300} # inteiro
conjunto3 = {True,False,False,True} #boolean
conjunto4 = {"simone", "Rua a","Iraja", 21980831997,54,"Pós Graduação"}

print(conjunto1)
print("------------------")
print(conjunto2)
print("------------------")
print(conjunto3)
print("------------------")
print(conjunto4)
print("------------------")