tenho_sede = True
tenho_fome = False

if tenho_fome and tenho_sede: 
    print("Comprar Sanduiche e Coca-Cola!")
elif tenho_sede and not tenho_fome:
    print("Comprar Coca-Cola!")
elif not(tenho_sede) and tenho_fome :
    print("Comprar Sanfuiche")
else:
    print("Não gastar dinheiro")
