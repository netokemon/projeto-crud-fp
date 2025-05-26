import pandas as pd
import os
from CRUD_cardapio import listar_pratos


arquivoPedido = "pedidos.json"
arquivoCardapio = "cardapio.json"


def criar_pedido():

    print("\n--- Criar novo pedido ---")

    if os.path.exists(arquivoCardapio) and os.path.getsize(arquivoCardapio) > 0: 
        print("\n--- Cardápio do Restaurante ---\n") 
        listar_pratos()
    else: 
        print("\nA ação não pode ser feita, nenhum prato está cadastrado no cardápio.")
        return
    

    lNomes = []
    lQuantidade = []

    
    while(True):

        if (len(lNomes)== 0): 
            nome = input("\nInsira o nome do prato: ")
            
        else: 
            opcao = input("\nDeseja inserir outro prato? ('Sim' / 'Não'): ")
            
            if opcao.lower() == "sim":
                nome = input("Insira o nome do prato: ")
            else:
                break


        df_cardapio = pd.read_json(arquivoCardapio)
        pratos_existentes = set(df_cardapio['nome'].tolist())

        while(nome not in pratos_existentes):
            print("O prato não existe no cardápio.")
            nome = input("Insira o nome do prato: ")

        quantidade = int(input("Insira a quantidade: "))
        
    
        if nome in lNomes:
            indexNome = lNomes.index(nome)
            lQuantidade[indexNome] += quantidade
        else:
            lNomes.append(nome)
            lQuantidade.append(quantidade)


    opcao = input("\nDeseja inserir uma observação adicional? ('Sim' / 'Não'): ")
    if opcao.lower() == "sim":
        observacaoAdicional = input("Insira a observação adicional: ")
    else: 
        observacaoAdicional = "Sem observação adicional"
    
    if os.path.exists(arquivoPedido) and os.path.getsize(arquivoPedido) > 0:
        df = pd.read_json(arquivoPedido)
        numeroPedido = int(df['numeroPedido'].max()) + 1
    else:
        numeroPedido = 1
        
    pedido = {
        "pratos" : lNomes,
        "quantidades" : lQuantidade,
        "numeroPedido": numeroPedido,
        "observaçãoAdicional": observacaoAdicional,
        "status": "Em preparo"
    }

    df = pd.DataFrame([pedido])
 
    if os.path.exists(arquivoPedido):

        if os.path.getsize(arquivoPedido) > 0:

            df_antigo = pd.read_json(arquivoPedido)
            df_final = pd.concat([df_antigo, df])
        else:
            df_final = df
 
        df_final.to_json(arquivoPedido, indent=4, orient='records')
   
    else:
        df.to_json(arquivoPedido, indent=4, orient='records')


def listar_pedidos():

    if os.path.exists(arquivoPedido) and os.path.getsize(arquivoPedido) > 0:

        df = pd.read_json(arquivoPedido)
        print("\n/////// Lista de Pedidos - Restauranty: ////////\n")

        for i in range(len(df)):

            print(f"\n//// Pedido número {df.loc[i, 'numeroPedido']} ////")
            pratos = df.loc[i, "pratos"]
            quantidades = df.loc[i, "quantidades"]

            for j in range(len(pratos)):
                print(f"\nPrato {j+1}: {pratos[j]} - {quantidades[j]} unidade(s)")
        
            observacao = df.loc[i, "observaçãoAdicional"]
            print(f"\nObservação adicional: {observacao}")

            status = df.loc[i, "status"]
            print(f"\nStatus: {status}")
            
        
    else:
        print("\n \n/////////////// ERRO: Sem pedidos até o momento! ////////////////////\n \n")


def atualizar_pedido():
    
    if os.path.exists(arquivoPedido) and os.path.getsize(arquivoPedido) > 0:

        df = pd.read_json(arquivoPedido, orient="records")

        print("\nLista de pedidos:\n")
        listar_pedidos()

        pedido_atualizar = int(input("\nInsira o número do pedido que deseja atualizar: "))

        if pedido_atualizar not in df["numeroPedido"].values:
            print("Esse pedido não existe.")
            return

        else:
            print("\nO que deseja atualizar?\n1- Pratos\n2- Observação adicional\n3- Status")
            opcao = int(input("Escolha sua opção: "))

            if opcao == 1:
                print("\nO que deseja fazer?\n1- Adicionar prato\n2- Remover prato\n3- Alterar quantidade de um prato")
                opcao = int(input("Escolha sua opção: "))

                if opcao == 1:
                    ...
                elif opcao == 2:
                    ...
                elif opcao == 3:
                    ...
                else: 
                    print("Opção inválida, selecione uma opção válida!")
                    return


            elif opcao == 2:
                print("\nO que deseja fazer?\n1- Adicionar descrição\n2- Remover descrição\n3- Alterar descrição")
                opcao = int(input("Escolha sua opção: "))

                if opcao == 1:
                    ...
                elif opcao == 2:
                    ...
                elif opcao == 3:
                    ...
                else:
                    print("Opção inválida, selecione uma opção válida!")
                    return

            elif opcao == 3:

                print("\nOpções de status:\n1- Em preparo\n2- Pronto\n3- Entregue")
                opcao = int(input("Escolha sua opção: "))


                if opcao == 1:
                    novo_status = "Em preparo"
                
                elif opcao == 2:
                    novo_status = "Pronto"
                
                elif opcao == 3:
                    novo_status = "Entregue"
                
                else:
                    print("Opção inválida, selecione uma opção válida!")
                    return
                   
                df.loc[df["numeroPedido"] == pedido_atualizar, "status"] = novo_status

        
            else: 
                print("\nOpção inválida, selecione uma opção válida!\n")
                return

            df.to_json(arquivoPedido, indent=4, orient="records")
            print("\nPedido atualizado com sucesso!\n")

    else:
        print("\n \n/////////////// ERRO: Sem pedidos até o momento! ////////////////////\n \n")
        return
        
            
            
        
def deletar_pedido():
    ...



def pedidos():
    while True:
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
            break
        
        else:
            print("\nOpção inválida, selecione uma opção válida!\n")
