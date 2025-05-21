import pandas as pd
import os
from CRUD_cardapio import listar_pratos

arquivoPedido = "pedidos.json"
arquivoCardapio = "cardapio.json"

def criar_pedido():

    print("\n--- Criar novo pedido ---")
    print("\n--- Cardápio do Restaurante ---")
   # listar_pratos()

    lNomes = []
    lQuantidade = []

    
    while(True):

        if (len(lNomes)== 0): 
            nome = input("Insira o nome do prato: ")
            
        else: 
            opcao = input("Deseja inserir outro prato? ('Sim' / 'Não'): ")
            
            if opcao == "Sim" or opcao == "sim" or opcao == "SIM":
                nome = input("Insira o nome do prato: ")
            else:
                break


        quantidade = int(input("Insira a quantidade: "))

        if nome in lNomes:
            indexNome = lNomes.index(nome)
            lQuantidade[indexNome] += quantidade
        else:
            lNomes.append(nome)
            lQuantidade.append(quantidade)


    pedido = {
        "pratos" : [lNomes],
        "quantidades" : [lQuantidade]
    }

    df = pd.DataFrame(pedido)

    # checando se o arquivo existe
    if os.path.exists(arquivoPedido):

        # checando se tem algo dentro do arquivo
        if os.path.getsize(arquivoPedido) > 0:

            # se tiver, ele pega o(s) pedido(s) existente(s) e concatena com o novo pedido
            df_antigo = pd.read_json(arquivoPedido)
            df_final = pd.concat([df_antigo, df])

        # se não tiver nada dentro do arquivo, ele coloca o novo pedido como primeiro item
        else:
            df_final = df

        # converte o pedido atualizado para json    
        df_final.to_json(arquivoPedido, indent=4, orient='records')

    # se o arquivo não existir, ele cria um e coloca o novo pedido dentro   
    else:
        df.to_json(arquivoPedido, indent=4, orient='records')


def listar_pedidos():

    if os.path.exists(arquivoPedido) and os.path.getsize(arquivoPedido) > 0:
        df = pd.read_json(arquivoPedido)
        print(df)
    else:
        print("Sem pedidos até o momento!")


def atualizar_pedido():
    ...

def deletar_pedido():
    ...



def pedidos():

    print("\n1- Criar pedido\n2- Listar pedidos\n3- Atualizar pedido\n4- Deletar pedido\n5- Voltar ao menu principal")
    opcao = int(input("Escolha sua opção: "))

    if opcao == 1:
        criar_pedido()

    elif opcao == 2:
        listar_pedidos()

    elif opcao == 3:
        atualizar_pedido()

    elif opcao == 4:
        deletar_pedido()

    elif opcao == 5:
        return
    
    else:
        print("\nOpção inválida, selecione uma opção válida!\n")
        pedidos()
