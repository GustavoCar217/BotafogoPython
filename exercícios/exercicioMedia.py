somatorio = 0
numeros = 0
while True:
    numero = int(input("Escreva um número(0 - saí): "))
    if numero == 0:
        break
    somatorio = somatorio + numero
    numeros = numeros + 1
print("Quantidade de números digitados:", numeros)
print("Total: ", somatorio)
print(f'Média: {somatorio/numeros}') 

