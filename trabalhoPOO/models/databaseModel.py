import sqlite3


class Database:
    def __init__(self, db_name="estoque.db"):
        self.__conn = sqlite3.connect(db_name)
        self.__cursor = self.__conn.cursor()
        self.__criar_tabela()

    def __criar_tabela(self):
        self.__cursor.execute("""
        CREATE TABLE IF NOT EXISTS Produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
        """)
        self.__conn.commit()

    def executar_comando(self, comando, parametros=()):
        self.__cursor.execute(comando, parametros)
        return self.__cursor.fetchall()

    def executar_alteracao(self, comando, parametros=()):
        self.__cursor.execute(comando, parametros)
        self.__conn.commit()

    def buscar(self, query):
        try:
            self.__cursor.execute(query)
            return self.__cursor.fetchall()
        except Exception as e:
            print(f"Erro ao executar a consulta: {e}")
            return None

    def fechar_conexao(self):
        self.__conn.close()
