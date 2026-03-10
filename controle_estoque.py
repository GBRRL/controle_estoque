estoque = {}
while True:
    print("\n=== CONTROLE DE ESTOQUE ===")
    print("1 - Registrar entrada de produto")
    print("2 - Registrar saída de produto")
    print("3 - Consultar estoque")
    print("4 - Encerrar sistema")
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        produto = input("Informe o nome do produto: ")
        quantidade = int(input("Informe a quantidade recebida: "))
        if produto in estoque:
            estoque[produto] += quantidade
        else:
            estoque[produto] = quantidade
        print("Entrada registrada com sucesso.")

    elif opcao == '2':
        produto = input("Informe o nome do produto: ")
        quantidade = int(input("Informe a quantidade retirada: "))
        if produto not in estoque:
            print("Produto não encontrado no estoque.")
        elif estoque[produto] < quantidade:
            print("Quantidade insuficiente em estoque para realizar a saída.")
        else:
            estoque[produto] -= quantidade
            print("Saída registrada com sucesso.")

    elif opcao == '3':
        print("\nEstoque atual:")
        for produto, quantidade in estoque.items():
            print(f"{produto}: {quantidade}")

    elif opcao == '4':
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")