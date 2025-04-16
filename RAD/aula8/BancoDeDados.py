import os 
import sqlite3
import Pessoa,Marca,Veiculo

class BancoDeDados:
    def __init__(self,nome_banco="banco.db"):
        self.nome_banco = os.path.join(os.path.dirname(__file__),nome_banco)
        self.conn = None

    def conectar(self):
        try:
            self.conn = sqlite3.connect(self.nome_banco)
        except sqlite3.Error as e:
            print(f"erro ao conectar ao banco de dados: {e}")
        except sqlite3.DatabaseError as dbe:
            print(f"erro ao criar o banco {dbe}")

    def criar_table(self):
        self.criar_tb_pessoa()
        self.criar_tb_marca()
        self.criar_tb_veiculo()

    def criar_tb_pessoa(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Pessoa (
                        cpf INTEGER PRIMARY KEY,
                        nome TEXT NOT NULL,
                        nascimento DATE,
                        oculos BOLLEAN
                        )"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"erro ao criar tabela pessoa {e}")
            except sqlite3.IntegrityError as it:
                print(f"erro de api {it}")

    def criar_tb_marca(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Marca (
                        id INTEGER PRIMARY KEY,
                        nome TEXT NOT NULL,
                        sigla TEXT 
                        )"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"erro ao criar tabela marca: {e}")

    def criar_tb_veiculo(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Veiculo(
                        placa TEXT PRIMARY KEY,
                        cor TEXT NOT NULL,
                        cpf_proprietario INTEGER,
                        id_marca INTEGER,
                        FOREIGN KEY (cpf_proprietario) REFERENCES Pessoa(cpf),
                        FOREIGN KEY (id_marca) REFERENCES (Marca(id))
                    )"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                print(f"erro ao criar tabela veiculo {e}")

            except sqlite3.OperationalError as op:
                print(f"erro ao criar tabela {op}")