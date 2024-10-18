alunos = int(input("Quantos alunos você quer ver a media"))
nome = input("Nome do aluno: ")
nota1 = float(input("Primeira nota tirada: "))
nota2 = float(input("Segunda nota tirada: "))

media = (nota1 + nota2)/2

if media >= 6.5:
    print(f"{media} - Aprovado")
else:
    print(f"{media} - Reprovado")