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
        print("\n/////////////// ERRO: A ação não pode ser feita, nenhum prato está cadastrado no cardápio. ///////////////")
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
            print("\n/////////////// ERRO: O prato não existe no cardápio. ///////////////")
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

print("\n---> Pedido Criado com sucesso! <---\n")



def listar_pedido_especifico(numeroPedido=None):
        
    if os.path.exists(arquivoPedido) and os.path.getsize(arquivoPedido) > 0:    

        df = pd.read_json(arquivoPedido)

        if numeroPedido is None:
            numeroPedido = int(input("\nInsira o número do pedido: "))

        
        if numeroPedido not in df["numeroPedido"].values:

            print("\n/////////////// ERRO: Esse pedido não existe. ///////////////\n")
            return
        
        else:

            index = df[df["numeroPedido"] == numeroPedido].index[0]

            print(f"\n//// Pedido n° {df.loc[index, 'numeroPedido']} ////")

            pratos = df.loc[index, "pratos"]
            quantidades = df.loc[index, "quantidades"]

            for j in range(len(pratos)):

                print(f"\nPrato {j+1}: {pratos[j]} - {quantidades[j]} unidade(s)")
            
            observacao = df.loc[index, "observaçãoAdicional"]
            print(f"\nObservação adicional: {observacao}")

            status = df.loc[index, "status"]
            print(f"\nStatus: {status}")

    else:
        print("\n \n/////////////// ERRO: Sem pedidos até o momento! ////////////////////\n \n")


def listar_todos_pedidos():

    df = pd.read_json(arquivoPedido)

    if os.path.exists(arquivoPedido) and os.path.getsize(arquivoPedido) > 0:

        print("\n/////// Lista de Pedidos - Restauranty: ////////\n")

        for i in range(len(df)):

            print(f"\n//// Pedido n° {df.loc[i, 'numeroPedido']} ////")

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


def listar_pedidos():

    if os.path.exists(arquivoPedido) and os.path.getsize(arquivoPedido) > 0:

        print("\nO que deseja listar?\n1- Pedido especifico\n2- Todos os pedidos")
        opcao = int(input())

        if opcao == 1:
            listar_pedido_especifico()
        elif opcao == 2:
            listar_todos_pedidos()
    
    else:
        print("\n \n/////////////// ERRO: Sem pedidos até o momento! ////////////////////\n \n")

 
def atualizar_pedido():
    
    if os.path.exists(arquivoPedido) and os.path.getsize(arquivoPedido) > 0:

        df = pd.read_json(arquivoPedido, orient="records")

        listar_todos_pedidos()

        pedido_atualizar = int(input("\nInsira o número do pedido que deseja atualizar: "))

        if pedido_atualizar not in df["numeroPedido"].values:

            print("\n/////////////// ERRO: Esse pedido não existe. ///////////////\n")
            return

        else:

            listar_pedido_especifico(pedido_atualizar)

            print("\nO que deseja atualizar?\n1- Pratos\n2- Observação adicional\n3- Status")
            opcao = int(input("Escolha sua opção: "))

            if opcao == 1:

                print("\nO que deseja fazer?\n1- Adicionar prato\n2- Remover prato\n3- Alterar quantidade de um prato")
                opcao = int(input("Escolha sua opção: "))

                if opcao == 1:

                    if os.path.exists(arquivoCardapio) and os.path.getsize(arquivoCardapio) > 0: 

                        print("\n--- Cardápio do Restaurante ---\n") 
                        listar_pratos()

                    else:

                        print("\n/////////////// ERRO: A ação não pode ser feita, nenhum prato está cadastrado no cardápio. ///////////////")
                        return
                    
                    nome = input("\nInsira o nome do prato: ")

                    df_cardapio = pd.read_json(arquivoCardapio)
                    pratos_existentes = set(df_cardapio['nome'].tolist())

                    while(nome not in pratos_existentes):
                        print("\n/////////////// ERRO: O prato não existe no cardápio. ///////////////")
                        nome = input("Insira o nome do prato: ")

                    quantidade = int(input("Insira a quantidade: "))
                    
                    if nome in df.loc[df["numeroPedido"] == pedido_atualizar, "pratos"].values[0]:

                        indexNome = df.loc[df["numeroPedido"] == pedido_atualizar, "pratos"].values[0].index(nome)
                        df.loc[df["numeroPedido"] == pedido_atualizar, "quantidades"].values[0][indexNome] += quantidade
                    
                    else:

                        df.loc[df["numeroPedido"] == pedido_atualizar, "pratos"].values[0].append(nome)
                        df.loc[df["numeroPedido"] == pedido_atualizar, "quantidades"].values[0].append(quantidade)

                elif opcao == 2:

                    nome = input("\nInsira o nome do prato que deseja remover: ")

                    if nome not in df.loc[df["numeroPedido"] == pedido_atualizar, "pratos"].values[0]:

                        print("\n/////////////// ERRO: Esse prato não está no pedido. ///////////////\n")
                        return
                    else:

                        indexNome = df.loc[df["numeroPedido"] == pedido_atualizar, "pratos"].values[0].index(nome)
                        df.loc[df["numeroPedido"] == pedido_atualizar, "pratos"].values[0].pop(indexNome)
                        df.loc[df["numeroPedido"] == pedido_atualizar, "quantidades"].values[0].pop(indexNome)

                elif opcao == 3:

                    nome = input("\nInsira o nome do prato que deseja alterar a quantidade: ")

                    if nome not in df.loc[df["numeroPedido"] == pedido_atualizar, "pratos"].values[0]:

                        print("\n/////////////// ERRO: Esse prato não está no pedido. ///////////////\n")
                        return
                    
                    else:

                        nova_quantidade = int(input("Insira a nova quantidade: "))
                        indexNome = df.loc[df["numeroPedido"] == pedido_atualizar, "pratos"].values[0].index(nome)
                        df.loc[df["numeroPedido"] == pedido_atualizar, "quantidades"].values[0][indexNome] = nova_quantidade
                else: 
                    print("\n/////////////// ERRO: Opção inválida, selecione uma opção válida! ///////////////\n")
                    return


            elif opcao == 2:
                print("\nO que deseja fazer?\n1- Adicionar observação\n2- Remover observação\n3- Alterar observação")
                opcao = int(input("Escolha sua opção: "))

                if opcao == 1:
                    nova_observação = input("Insira a observação: ")
                elif opcao == 2:
                    nova_observação = "Sem observação adicional"
                elif opcao == 3:
                    nova_observação = input("Insira a nova observação: ")
                else:
                    print("\n/////////////// ERRO: Opção inválida, selecione uma opção válida! ///////////////\n")
                    return
                
                df.loc[df["numeroPedido"] == pedido_atualizar, "observaçãoAdicional"] = nova_observação

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
                    print("\n/////////////// ERRO: Opção inválida, selecione uma opção válida! ///////////////\n")
                    return
                   
                df.loc[df["numeroPedido"] == pedido_atualizar, "status"] = novo_status

        
            else: 
                print("\n/////////////// ERRO: Opção inválida, selecione uma opção válida! ///////////////\n")
                return

            df.to_json(arquivoPedido, indent=4, orient="records")
            print("\nPedido atualizado com sucesso!\n")

    else:
        print("\n \n/////////////// ERRO: Sem pedidos até o momento! ////////////////////\n \n")
        return
        
                      
def deletar_pedido():

    if os.path.exists(arquivoPedido) and os.path.getsize(arquivoPedido) > 0:

        df = pd.read_json(arquivoPedido, orient="records")
        listar_pedidos()

        pedido_deletar = int(input("\nInsira o número do pedido que deseja deletar: "))

        if pedido_deletar not in df["numeroPedido"].values:
            print("/////////////// ERRO: Esse pedido não existe. ///////////////")
            return
        else:
            df = df[df["numeroPedido"] != pedido_deletar]

        df.to_json(arquivoPedido, indent=4, orient="records")
        print("\nPedido deletado com sucesso! :)\n")


def pedidos():
    print("\033[1;35m")
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
            print("\n/////////////// ERRO: Opção inválida, selecione uma opção válida! ///////////////\n")
    print("\033[0m")
