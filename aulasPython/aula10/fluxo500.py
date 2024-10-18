somatorio = 0
numeros = 0
while True:
    numero = int(input("Digite os numeros(0 - saí): "))
    if numero == 0:
        break
    somatorio = somatorio + numero
    numeros = numeros + 1
print(somatorio/numeros)