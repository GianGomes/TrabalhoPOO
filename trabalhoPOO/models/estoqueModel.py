from models.databaseModel import Database


class ControleEstoque:
    def __init__(self):
        self.db = Database()

    def adicionar_produto(self, nome, quantidade, preco):
        self.db.executar_alteracao("""
        INSERT INTO Produtos (nome, quantidade, preco) 
        VALUES (?, ?, ?)
        """, (nome, quantidade, preco))
        print("Produto adicionado com sucesso!")

    def listar_produtos(self):
        produtos = self.db.buscar("SELECT * FROM Produtos")
        for produto in produtos:
            print(
                f"ID: {produto[0]}, Nome: {produto[1]}, Quantidade: {produto[2]}, Preço: {produto[3]:.2f}")

    def atualizar_produto(self, id, quantidade=None, preco=None):
        if quantidade is not None:
            self.db.executar_alteracao(
                "UPDATE Produtos SET quantidade = ? WHERE id = ?", (quantidade, id))
        if preco is not None:
            self.db.executar_alteracao(
                "UPDATE Produtos SET preco = ? WHERE id = ?", (preco, id))
        print("Produto atualizado com sucesso!")

    def remover_produto(self, id):
        self.db.executar_alteracao(f"DELETE FROM Produtos WHERE id = {id}")
        print("Produto removido com sucesso!")

    def buscar_produto(self, id=None, nome=None):
        if id is not None:
            produtos = self.db.buscar(
                f"SELECT * FROM Produtos WHERE id = {id}")
        elif nome is not None:
            produtos = self.db.buscar(
                f"SELECT * FROM Produtos WHERE nome LIKE '%{nome}%'")
        else:
            print("Informe um ID ou Nome para buscar o produto.")
            return

        if produtos:
            for produto in produtos:
                print(
                    f"ID: {produto[0]}, Nome: {produto[1]}, Quantidade: {produto[2]}, Preço: {produto[3]:.2f}")
        else:
            print("Produto não encontrado.")

    def comprar_produto(self, id, quantidade):
        produtos = self.db.buscar(
            f"SELECT quantidade FROM Produtos WHERE id = {id}")
        if produtos:
            quantidade_atual = produtos[0][0]
            nova_quantidade = quantidade_atual - quantidade
            self.db.executar_alteracao(
                "UPDATE Produtos SET quantidade = ? WHERE id = ?", (nova_quantidade, id))
            print(
                f"Compra realizada com sucesso! Nova quantidade: {nova_quantidade}")
        else:
            print("Produto não encontrado.")

    def fechar_conexao(self):
        self.db.fechar_conexao()
