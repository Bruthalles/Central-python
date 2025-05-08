import sqlite3 as sq
import os

class BancoDeDados:
    def __init__(self):
        self.conn = None
    
    def conectar_banco(self):
        path = os.path.join(os.path.dirname(__file__),'banco.db')
        self.conn = sq.connect(path)
    
    def fechar_conexao(self):
        if self.conn:
            self.conn.close()
            self.conn = None
    
    def criar_tabela(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute('''CREATE TABLE usuario(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            email TEXT NOT NULL,
                            senha TEXT NOT NULL )''')
                cursor.commit()
            except sq.Error as e:
                print(f"erro ao criar tabela: {e}")