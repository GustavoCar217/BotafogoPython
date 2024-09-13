import math
salario = float (input("Qual o seu Salário? :"))
porcentagem = float (input("Qual a Porcentagem? :"))
resultado = float ((salario * porcentagem)/100)
print("Aumento de :", resultado)
print("Salário Final :",salario + resultado)