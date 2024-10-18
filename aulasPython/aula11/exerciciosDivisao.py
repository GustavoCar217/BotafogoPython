resposta = 'S'
while resposta == 'S':
    notas = int(input("Digite um valor: "))
    n50 = notas // 50
    r50 = notas % 50
    no10 = r50 // 10
    n1 = r50 % 10
    print('Total de Notas de 50 =', n50 )
    print('Total de Notas de 10 =', no10 )
    print('Total de Moedas de 1 =', n1 )
    resposta = input('Deseja fazer outro saque (S/N)? ')

    # if resposta == 'N': (teoricamente tosco)
    #     break
