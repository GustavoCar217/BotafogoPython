def maior_numero(lista_numero):
    lista_numero.sort()
    lista_numero.reverse()
    maior_numero = lista_numero[0]
    return maior_numero


resultado = maior_numero([50,5,80,9000,30,33,90])
print(resultado)

