import pandas as pd
import os

arquivoCardapio = "cardapio.json"

def criar_prato():
    print("\nCriar novo prato")
    nome = input("Nome do prato: ").capitalize()
    descricao = input("Descrição do prato: ")
    ingredientes = input("Ingredientes do prato: ")
    categoria = input("Categoria do prato: ")
    valor = float(input("Valor do prato: "))
    prato = {
        "nome": [nome],
        "descricao": [descricao],
        "ingredientes": [ingredientes],
        "categoria": [categoria],
        "valor": [valor]
    }
    df_atual = pd.DataFrame(prato)

    if os.path.exists(arquivoCardapio):
        if os.path.getsize(arquivoCardapio) > 0:
            df_antigo = pd.read_json(arquivoCardapio)
            df_final = pd.concat([df_antigo, df_atual])
        else:
            df_final = df_atual
    else:
        df_final = df_atual

    df_final.to_json(arquivoCardapio, indent=4, orient="records")
    print(f"\n---> Prato '{nome}' criado com sucesso! <---")


def listar_pratos():
    if os.path.exists(arquivoCardapio):
        if os.path.getsize(arquivoCardapio) > 0:
            df = pd.read_json("cardapio.json")
            print(df)
        
    else:
     print ("Cardápio não existe!!")
   


def atualizar_prato():
    if os.path.exists(arquivoCardapio):
        df = pd.read_json(arquivoCardapio, orient="records")
        print("\nCardápio atual: ")
        print(df)
        prato_atualizar = input("\nDigite o nome do prato que deseja atualizar: ")

        if prato_atualizar not in df["nome"].values:
            print("Este prato não existe no cardápio.")
            return atualizar_prato()
        else:
            print("\nO que deseja atualizar?\n1- Nome\n2- Descrição\n3- Categoria\n4- Ingredientes\n5 - Valor")
            opcao = int(input("Escolha sua opção: "))

            if opcao == 1:
                novo_nome = input("Novo nome do prato: ")
                df.loc[df["nome"] == prato_atualizar, "nome"] = novo_nome
            elif opcao == 2:
                nova_descricao = input("Nova descrição do prato: ")
                df.loc[df["nome"] == prato_atualizar, "descricao"] = nova_descricao
            elif opcao == 3:
                nova_categoria = input("Nova categoria do prato: ")
                df.loc[df["nome"] == prato_atualizar, "categoria"] = nova_categoria
            elif opcao == 4:
                novos_ingredientes = float(input("Novos ingredientes do prato: "))
                df.loc[df["nome"] == prato_atualizar, "ingredientes"] = novos_ingredientes
            elif opcao == 5:
                novo_valor = float(input("Novo valor do prato: "))
                df.loc[df["nome"] == prato_atualizar, "valor"] = novo_valor
            else:
                print("\nOpção inválida, tente novamente.")
                return atualizar_prato()

            df.to_json(arquivoCardapio, indent=4, orient="records")
            print(f"\nPrato '{prato_atualizar}' atualizado com sucesso!")
    else:
        print("\nNenhum prato cadastrado no cardápio.")
        return

def deletar_prato():
    if os.path.exists(arquivoCardapio):
        df = pd.read_json(arquivoCardapio, orient="records")
        print("\nCardápio atual: ")
        print(df)
        prato_deletar = input("\nDigite o nome do prato que deseja deletar: ")

        if prato_deletar not in df["nome"].values:
            print("Este prato não existe no cardápio.")
            return deletar_prato()
        else:
            df = df[df["nome"] != prato_deletar]

            df.to_json(arquivoCardapio, indent=4, orient="records")
            print(f"\nPrato '{prato_deletar}' deletado com sucesso!")
    else:
        print("\nNenhum prato cadastrado no cardápio.")
        return
    
def buscar_prato():
     if os.path.exists(arquivoCardapio):
        if os.path.getsize(arquivoCardapio) > 0:
          df = pd.read_json(arquivoCardapio, orient="records")
          nome_prato = input("Digite o nome do prato que deseja buscar: ").capitalize()

        if nome_prato in df["nome"].values:
            prato = df[df["nome"] == nome_prato]
            print("\nPrato encontrado:")
            print(prato)

        else:
            print("\nPrato não encontrado no cardápio.")

def cardapio():
    print("\033[31m")
    while True: 
        print("\n1- Criar novo prato\n2- Listar pratos\n3- Atualizar prato\n4- Deletar prato\n5- Buscar prato\n6- Voltar ao menu principal")
        opcao = int(input("Escolha sua opção: "))
        if opcao == 1:
            criar_prato()
        elif opcao == 2:
            listar_pratos()
        elif opcao == 3:
            atualizar_prato()
        elif opcao == 4:
            deletar_prato()
        elif opcao == 5:
            buscar_prato()
        elif opcao == 6:
            break
        else:
            print("\nOpção inválida, selecione uma opção válida!\n")
            continue
    print("\033[0m")

