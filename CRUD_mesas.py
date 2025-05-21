import pandas as pd
import os

arquivo_mesas = "mesas.json"

def adicionar_mesas():
    print("\nAdicionar uma nova mesa")
    numero = int(input("Insira o número da mesa: "))
    estado = int(input("Insira o estado da mesa\n0- Livre\n1- Ocupado\n2- Reservado\nSelecione uma opção: "))
    mesa = {
        "numero": [numero],
        "estado": [estado]
    }

    df_atual = pd.DataFrame(mesa)

    if os.path.exists(arquivo_mesas):
        df_antigo = pd.read_json(arquivo_mesas)

        if os.path.getsize(arquivo_mesas) > 0:

            if df_antigo[df_atual['numero'] == df_antigo['numero']].empty:
                df_final = pd.concat([df_antigo, df_atual])
            else:
                print ("Uma mesa com esse número já existe. Crie outra mesa com um número válido.\n")
                adicionar_mesas()

        else:
            df_final = df_atual
    
    else:
        df_final = df_atual

    df_final.to_json(arquivo_mesas, indent=4, orient='records')

    print(f"\Mesa de número '{numero}' criada com sucesso!")

    def listar_mesas():
        df = pd.read_json(arquivo_mesas)
        print(df)

def ler_mapa_mesas():
    if not os.path.exists(arquivo_mesas) or os.path.getsize(arquivo_mesas) == 0:
        print("\nNenhuma mesa cadastrada ainda.")
        return
    
    df = pd.read_json(arquivo_mesas)

    estado_desc = {
        0: "Livre",
        1: "Ocupada",
        2: "Reservada"
    }

    print("\nMapa de mesas do restaurante")

    df = df.sort_values('numero')
    for _, row in df.iterrows():
        numero = row['numero']
        estado = estado_desc[row['estado']]
        print (f"Mesa {numero}: {estado}")

    print ("\nResumo de status: ")
    for cod, desc in estado_desc.items():
        count = len(df[df['estado'] == cod])
        print (f"{desc}: {count} mesa(s)")

def atualizar_mesas():
    if not os.path.exists(arquivo_mesas) or os.path.getsize(arquivo_mesas) == 0:
        print("\nNenhuma mesa cadastrada ainda.")
        return

    df = pd.read_json(arquivo_mesas)

    print("\nAtualização de mesas")
    print ("\nMesas disponíveis: ")
    print (df[['numero', 'estado']].to_string(index=False))

    try:
        numero_mesa = int(input("\nInsira o número da mesa para atualizar: "))
    except ValueError:
        print("\nNúmero inválido. Digite apenas números.")
        return atualizar_mesas()
    
    if numero_mesa not in df['numero'].values:
        print(f"\nMesa {numero_mesa} não encontrada.")
        return

    print ("\nQual categoria deseja atualizar?")
    print ("1- Número")
    print ("2- Estado")

    try:
        opcao = int(input("Escolha sua opção: "))
    except ValueError:
        print ("\nOpção inválida.")
        return

    if opcao == 1:
        try:
            novo_numero = int(input("Digite o novo número da mesa: "))

            if novo_numero in df['numero'].values:
                print("\nJá existe uma mesa com este número.")
                return

            df.loc[df['numero'] == numero_mesa, 'numero '] = novo_numero
            print (f"\nNúmero da mesa {numero_mesa} atualizado para {novo_numero} com sucesso!")

        except ValueError:
            print ("\nNúmero inválido.")
            return

    elif opcao == 2:
        print ("\nQual será o novo estado?")
        print ("0- Livre")
        print ("1- Reservada")
        print ("2- Ocupada")

        try:
            novo_estado = int(input("Escolha sua opção: "))

            if novo_estado not in [0, 1, 2]:
                print ("\nOpção inválida.")
                return

            df.loc[df['numero'] == numero_mesa, 'estado'] = novo_estado

            estados = {0: "Livre", 1: "Reservada", 2: "Ocupada"}
            print(f"\nEstado da mesa {numero_mesa} atualizado para '{estados[novo_estado]}' com sucesso!")

        except ValueError:
            print ("\nOpção inválida.")
            return

    else:
        print("\nOpção inválida.")
        return
    
    df.to_json(arquivo_mesas, ident=4, orient='records')
    print("\nMesa atualizada com sucesso! :)")

def remover_mesas():
    ...

def mesas():
    print("\nGerenciamento das mesas\n")
    print("\n1- Adicionar nova mesa\n2- Ler mapa de mesas\n3- Atualizar status da mesa\n4- Remover mesa\nVoltar ao menu principal")
    opcao = int(input("Escolha sua opção: "))
    if opcao == 1:
        adicionar_mesas()
    elif opcao == 2:
        ler_mapa_mesas()
    elif opcao == 3:
        atualizar_mesas()
    elif opcao == 4:
        remover_mesas
    elif opcao == 5:
        return
    else:
        print ("\nOpção inválida, selecione uma opção válida!\n")
        mesas()