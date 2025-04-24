import sqlite3
import os
from backend.classes.ContaBancaria import Usuario

class BancoDeDados:
    def __init__(self,erro,nome_banco="banco.db"):
        self.nome_banco = os.path.join(os.path.dirname(__file__),nome_banco)
        self.conn = None
        self.erro = None
    
    def conectar(self):
        try:
            self.conn = sqlite3.connect(self.nome_banco)
        except sqlite3.Error as e :
            self.erro = f"erro ao conectar ao banco de dados: {e}"
        except sqlite3.DatabaseError as dbe:
            self.erro = f"erro ao criar o banco {dbe}"
    
    def criar_table(self):
        self.criar_tb_user()
    
    def criar_tb_user(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Usuario(
                        id INTEGER PRIMARY KEY,
                        email TEXT NOT NULL UNIQUE,
                        senha TEXT NOT NULL UNIQUE)"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                self.erro = f"erro ao criar table usuario {e}"
            except sqlite3.IntegrityError as ie:
                self.erro = f"erro de api {ie}"