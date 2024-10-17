num1 = float (input("Primeiro número para realizar a conta: "))
num2 = float (input("Segundo número para realizar a conta: "))
operador = (input("Operador matematico( +,-,*,/): "))
if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    resultado = num1 / num2
print("Total :",resultado)
