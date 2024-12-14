from models.estoqueModel import ControleEstoque


def main():
    print("\n--- Controle de Estoque ---")
    print("1. Adicionar Produto")
    print("2. Listar Produtos")
    print("3. Atualizar Produto")
    print("4. Remover Produto")
    print("5. Buscar Produto")
    print("6. Comprar Produto")
    print("0. Sair")
    return input("Escolha uma opção: ")


if __name__ == "__main__":
    controle = ControleEstoque()

    while True:
        opcao = main()
        if opcao == "1":
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            controle.adicionar_produto(nome, quantidade, preco)
        elif opcao == "2":
            controle.listar_produtos()
        elif opcao == "3":
            id = int(input("ID do produto: "))
            quantidade = input(
                "Nova quantidade (deixe vazio para não alterar): ")
            preco = input("Novo preço (deixe vazio para não alterar): ")
            controle.atualizar_produto(
                id,
                quantidade=int(quantidade) if quantidade else None,
                preco=float(preco) if preco else None
            )
        elif opcao == "4":
            id = int(input("ID do produto a remover: "))
            controle.remover_produto(id)
        elif opcao == "5":
            tipo_busca = input("Buscar por (1) ID ou (2) Nome? ")
            if tipo_busca == "1":
                id = int(input("ID: "))
                controle.buscar_produto(id=id)
            elif tipo_busca == "2":
                nome = input("Nome: ")
                controle.buscar_produto(nome=nome)
        elif opcao == "6":
            id = int(input("ID do produto: "))
            quantidade = int(input("Quantidade comprada: "))
            controle.comprar_produto(id, quantidade)
        elif opcao == "0":
            controle.fechar_conexao()
            print("Fechando o sistema, até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
