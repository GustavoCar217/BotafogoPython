def exibir_status(palavra, lcorretas):
    status = ''
    for letra in palavra:
        if letra in lcorretas:
            status += letra
        else:
            status += '_'
    return status
def definir_dificuldade():
    dificuldade = input('Qual a dificuldade desejada? \n f= Fácil\n m= Médio\n d= Difícil\n').lower()
    if dificuldade == "f":
        numero = 7
    elif dificuldade == "m":
        numero = 5 
    elif dificuldade == "d":
        numero = 3
    else:
        print("dificuldade inválida")
        return definir_dificuldade()
    return numero

def jogo_forca():
    palavra = input('Digite a palavra secreta\n').lower()
    lcorretas = set()
    lerradas = set()
    tentativas = definir_dificuldade

    print("\nBem-vindo ao jogo de Forca!")
    print('A palavra tem', len(palavra), 'letras.')

    while tentativas > 0:
        print("\nPalavra:", exibir_status(palavra, lcorretas))
        print('Tentativas restantes:', tentativas)
        print('Letras erradas:', ','.join(lerradas))
               
        letra = input('Digite uma letra: ').lower()

        if letra in lcorretas or letra in lerradas:
            print('Você já tentou essa letra')
            continue
    
        if letra in palavra:
            lcorretas.add(letra)
            if set(palavra) == lcorretas:
                print('\nParabéns! Você acertou a palávra:', palavra)
        else:
            lerradas.add(letra)
            tentativas -= 1
    if tentativas ==0:
        print('\nVocê perdeu! À palavra era: ', palavra)
    
jogo_forca()