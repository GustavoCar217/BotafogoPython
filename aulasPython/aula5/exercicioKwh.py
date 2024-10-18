kwh = int(input("Quantidade consumida em Kwh? "))
lugar = input("Lugar da instalação (R), (C), (I)? ")
if lugar == "R" or "r":
    if kwh <= 500:
        resultado = 0.40
    else:
        resultado = 0.65
elif lugar == "C" or "c":
    if kwh <= 1000:
        resultado = 0.55
    else:
        resultado = 0.60
elif lugar == "I" or "i":
    if kwh <= 5000:
        resultado = 0.70
    else:
        resultado = 0.80
else :
    resultado = 0
    print("Erro !")
custo = kwh * resultado
print(f'O valor a pagar R$ {custo}')