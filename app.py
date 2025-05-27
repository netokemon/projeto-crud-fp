from CRUD_cardapio import cardapio
from CRUD_pedidos import pedidos
from CRUD_mesas import mesas


while True:
    
    print("\033[1;34m")
    print("\n////// Restauranty - Gerenciamento \\\\\\\\\\\\")
    opcao = int(input("\n    \n1- Gerenciar cardápio\n2-Gerenciar mesas\n3-Gerenciar pedidos\nEscolha sua opção: "))
    if opcao == 1:
        cardapio()
    elif opcao == 2:
        mesas()
    elif opcao == 3:
        pedidos()
    else:
        print("\n/////////////// ERRO: Opção inválida, selecione uma opção válida! ///////////////\n")
        continue