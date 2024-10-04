altura = float(input('Digite sua Altura: '))
sexo = input('Digite seu sexo(M/F): ')
if sexo == 'M':
    peso = (72.7 * altura) - 58
    # print(f"Peso ideal de : {peso:.2f}") (forma mais longa de resolver)
else :
    peso = (62.1 * altura) - 44.7
    # print(f"Peso ideal de : {peso:.2f}") (não há necessidade)
print(f"Seu peso ideal é de: {peso:.2f}")