import math
valor_produto = float (input("Valor do Produto?: "))
valor_desconto =float (input("Valor de Desconto?: "))
desconto =float (valor_desconto/100)
print("Desconto de :", desconto * valor_produto,)
print("Valor Final do Produto: ", (valor_produto) - desconto * valor_produto)