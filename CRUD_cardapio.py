import pandas as pd

def criar_prato():
    print("\nCriar novo prato")
    nome = input("Nome do prato: ")
    descricao = input("Descrição do prato: ")
    categoria = input("Categoria do prato: ")
    valor = float(input("Valor do prato: "))
    prato = {
        "nome": [nome],
        "descricao": [descricao],
        "categoria": [categoria],
        "valor": [valor]
    }
    df = pd.DataFrame(prato)
    df.to_json("cardapio.json")

    print(f"\nPrato '{nome}' criado com sucesso!")


def listar_pratos():
    df = pd.read_json("cardapio.json")
    print(df)


def atualizar_prato():
    ...

def deletar_prato():
    ...

def cardapio():
    print("\n1- Criar novo prato\n2- Listar pratos\n3- Atualizar prato\n4- Deletar prato\n5- Voltar ao menu principal")
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
        return
    else:
        print("\nOpção inválida, selecione uma opção válida!\n")
        cardapio()