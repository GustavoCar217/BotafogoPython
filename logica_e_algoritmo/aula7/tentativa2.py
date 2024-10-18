# while precisa de um contador ativo
# alunos = int(input("Quantos alunos deseja calcular a media: "))
# i = 0
# while i < alunos:
#     nome = input("Nome do aluno: ")
#     nota1 = float(input("Primeira nota tirada: "))
#     nota2 = float(input("Segunda nota tirada: "))
#     media = (nota1 + nota2)/2

#     if media >= 6.5:
#         print(f"{media} - Aprovado")
#     else:
#         print(f"{media} - Reprovado")
   
#     i +=1
# for faz de uma forma mais "rapida" sem precisar de contador
alunos = int(input("Quantos alunos deseja calcular a media: "))
for i in range(alunos):
    nome = input("Nome do aluno: ")
    nota1 = float(input("Primeira nota tirada: "))
    nota2 = float(input("Segunda nota tirada: "))
    media = (nota1 + nota2)/2

    if media >= 6.5:
        print(f"{media} - Aprovado")
    else:
        print(f"{media} - Reprovado")
    