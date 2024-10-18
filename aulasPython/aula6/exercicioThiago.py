# Atividade Thiago Dalicio

# Atividade 1 - Calcular o preço de energia elétrica
def atividade_1():
    # Pergunta a quantidade de kWh consumida e o tipo de instalação
    kwh = float(input("Informe a quantidade de kWh consumida: "))
    tipo_instalacao = input("Informe o tipo de instalação (R para residencial, C para comercial, I para industrial): ").upper()

    # Verifica o tipo de instalação e calcula o preço
    if tipo_instalacao == 'R':  # Residencial
        if kwh <= 500:
            preco = kwh * 0.40
        else:
            preco = kwh * 0.65
    elif tipo_instalacao == 'C':  # Comercial
        if kwh <= 1000:
            preco = kwh * 0.55
        else:
            preco = kwh * 0.60
    elif tipo_instalacao == 'I':  # Industrial
        if kwh <= 5000:
            preco = kwh * 0.70
        else:
            preco = kwh * 0.80
    else:
        print("Tipo de instalação inválido.")
        return

    # Exibe o valor a pagar
    print(f"O preço a pagar pelo consumo de {kwh} kWh é R$ {preco:.2f}")

# Atividade 2 - Contagem regressiva para o lançamento de um foguete
def atividade_2():
    # Contagem regressiva de 10 a 0 e imprime "Fogo!"
    for i in range(10, -1, -1):
        print(i)
    print("Fogo!")

# Atividade 3 - Ler números e calcular soma, quantidade e média
def atividade_3():
    # Inicializa variáveis
    soma = 0
    quantidade = 0

    # Lê números até o usuário digitar 0
    while True:
        numero = int(input("Digite um número (0 para sair): "))
        if numero == 0:
            break
        soma += numero
        quantidade += 1

    # Exibe os resultados
    if quantidade > 0:
        media = soma / quantidade
        print(f"Você digitou {quantidade} números.")
        print(f"A soma dos números é {soma}.")
        print(f"A média dos números é {media:.2f}.")
    else:
        print("Nenhum número foi digitado.")

# Menu 
def menu():
    while True:
        print("\nSelecione uma opção:")
        print("1 - Calcular o preço de energia elétrica (Atividade 1)")
        print("2 - Contagem regressiva para o lançamento de um foguete (Atividade 2)")
        print("3 - Ler números e calcular soma, quantidade e média (Atividade 3)")
        print("0 - Sair")
        
        opcao = input("Digite sua opção: ")

        if opcao == '1':
            atividade_1()
        elif opcao == '2':
            atividade_2()
        elif opcao == '3':
            atividade_3()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

# Executa o menu
menu()

# Dica de livro, programador pragmático, código limpo
