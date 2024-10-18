# Usando mais espaço em disco
# salario = float (input("Digite o valor do salário do funcionário "))
# porcentagem = float (10)
# porcentagem2 = float (15)
# salario_novo1=(salario * porcentagem)/100 + salario
# salario_novo2=(salario * porcentagem2)/100 + salario
# if salario <= 1250:
#     print(f'novo salario de R$: {salario_novo1}')
# else:
#     print(f'novo salario de R$: {salario_novo2}')   

# forma que consome menos 
salario = float(input("Digite o valor do salário do funcionário"))
if salario <= 1250 :
  #  salario = salario + (salario *15)/100
    salario = salario * 1.15
    print(f'O valor do novo salário é R$ {salario}')
else:
    salario = salario * 1.1
    print(f'O valor do novo salario é R$ {salario}')