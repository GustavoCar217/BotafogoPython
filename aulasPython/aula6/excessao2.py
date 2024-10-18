try:
    n1 = int(input("Digite o primeiro número"))
    print(n1)
    n2 = int(input("Digite o segundo número"))
    print(n2)

    calculo = n1/n2
    print("Resultado da divisão",calculo)

except ValueError:
    print('Digite um valor númerico')
except ZeroDivisionError:
    print("Não é possível dividir por zero")
except:
    print("Erro inesperado")
finally:
    print("------------")
    print("Sempre executará... entrando ou não dentro de uma excessão")