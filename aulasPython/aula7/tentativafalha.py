
alunos = int(input("Quantos alunos deseja calcular a media (0 saí)"))
resultado = alunos +1
while True:
    nome = input("Nome do aluno: ")
    nota1 = float(input("Primeira nota tirada: "))
    nota2 = float(input("Segunda nota tirada: "))
    media = (nota1 + nota2)/2

    if media >= 6.5:
        print(f"{media} - Aprovado")
    else:
        print(f"{media} - Reprovado")
    if resultado == alunos:
        break