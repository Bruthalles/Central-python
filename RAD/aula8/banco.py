import os 
import sqlite3
from Pessoa import Pessoa
from Veiculo import Veiculo
from Marca import Marca
import logging
import time 

#definindo caminho do log
path = os.path.join(os.path.dirname(__file__),'app.log')

logging.basicConfig(
    filename=path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def limpar_log():
    
    try:
        with open(path,'w') as a:
            time.sleep(180)
            a.write('')
    except FileNotFoundError as fle:
        log_error(f'erro ao limpar log {fle}')

def log_error(message):
    logging.error(message)
    

class BancoDeDados:
    def __init__(self,nome_banco="banco.db"):
        self.nome_banco = os.path.join(os.path.dirname(__file__),nome_banco)
        self.conn = None

    def conectar(self):
        try:
            self.conn = sqlite3.connect(self.nome_banco)
        except sqlite3.Error as e:
            
            log_error(f"erro ao conectar ao banco de dados: {e}")
        except sqlite3.DatabaseError as dbe:
            
            log_error(f"erro ao criar o banco {dbe}")

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
                        cpf INTEGER PRIMARY KEY NOT NULL,
                        nome TEXT NOT NULL,
                        nascimento DATE,
                        oculos BOLLEAN
                        )"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                log_error(f"erro ao criar tabela pessoa {e}")
            except sqlite3.IntegrityError as it:
                log_error(f"erro de api {it}")

    def criar_tb_marca(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Marca (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        sigla TEXT 
                        )"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                log_error(f"erro ao criar tabela marca: {e}")

    def criar_tb_veiculo(self):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    """CREATE TABLE IF NOT EXISTS Veiculo(
                        placa TEXT PRIMARY KEY NOT NULL,
                        cor TEXT NOT NULL,
                        cpf_proprietario INTEGER,
                        id_marca INTEGER,
                        FOREIGN KEY (cpf_proprietario) REFERENCES Pessoa(cpf),
                        FOREIGN KEY (id_marca) REFERENCES Marca(id)
                        )"""
                )
                self.conn.commit()
            except sqlite3.Error as e:
                log_error(f"erro ao criar tabela veiculo {e}")

            except sqlite3.OperationalError as op:
                log_error(f"erro ao criar tabela {op}")

    def inserir_pessoa(self,pessoa:Pessoa):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO Pessoa VALUES (?,?,?,?)",
                               (pessoa.cpf,pessoa.nome,pessoa.nascimento,pessoa.oculos),)
                self.conn.commit()
            except sqlite3.Error as e:
                log_error(f"erro inserir pessoa {e}")
    
    def inserir_veiculo(self,veiculo: Veiculo):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO Veiculo VALUES (?,?,?,?)",
                               (
                                   veiculo.placa,
                                   veiculo.cor,
                                   veiculo.proprietario.cpf,
                                   veiculo.marca.id,
                               ),
                )
                self.conn.commit()
            except sqlite3.Error as e:
                log_error(f"Erro ao inserir veículo: {e}")

    def inserir_marca(self,marca: Marca):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("INSERT INTO Marca VALUES (?,?,?)",
                (
                      marca.id,
                      marca.nome,
                      marca.sigla,),
                )
                self.conn.commit()
            except sqlite3.Error as e:
                log_error(e)
                

    def atualizar_pessoa(self,pessoa):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute(
                    "UPDATE Pessoa SET nome=?,nascimento=?,oculos=?,WHERE cpf=?",
			(pessoa.nome,
			pessoa.nascimento,
			pessoa.oculos),
                )
                self.conn.commit()
            except sqlite3.Error as e:
                log_error(f"Error ao inserir pessoa: {e}")

    def atualizar_marca(self, marca):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("UPDATE Pessoa SET id=?,nome=?,sigla=?",(
                    marca.id,
                    marca.nome,
                    marca.sigla),
                    )
                self.conn.commit()
            except sqlite3.Error as e:
                log_error(e)


    def atualizar_veiculo(self,veiculo):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("UPDATE Veiculo SET cor=?,cpf_proprietario=?,id_marca=? WHERE placa=?",
                           (
                               veiculo.cor,
                               veiculo.proprietario.cpf,
                               veiculo.marca.id,
                               veiculo.placa,
                           ),
                           )
                self.conn.commit()
            except sqlite3.Error as e:
                log_error(e)

    def apagar_veiculo(self,veiculo):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("DELETE FROM Veiculo WHERE placa=?",(veiculo.placa,))
                self.conn.commit()
            except sqlite3.Error as e:
                log_error(f"Erro ao apagar veiculo: {e}")

    def buscar_todas_pessoas(self):
        pessoas = []

        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM Pessoa")
                for row in cursor.fetchall():
                    cpf,nome,nascimento,oculos = row
                    pessoas.append(Pessoa(cpf,nome,nascimento,oculos))
            except sqlite3.Error as e:
                log_error(f"erro ao buscar pessoas: {e}")
        return pessoas
    
    def buscar_todas_marcas(self):
        marcas = []

        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM Marca")
                for row in cursor.fetchall():
                    id,nome,sigla = row
                    marcas.append(Marca(id,nome,sigla))

            except sqlite3.Error as e:
                log_error(f"erro ao buscar marcas: {e}")
        return marcas
    
    def buscar_todos_veiculos(self):
        veiculos =[]
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT *FROM Veiculo")
                for row in cursor.fetchall():
                    placa,cor,cpf_proprietario,id_marca = row
                    proprietario = self.buscar_pessoa_por_cpf(cpf_proprietario)
                    marca = self.buscar_marca_por_id(id_marca)
                    veiculos.append(Veiculo(placa,cor,marca,proprietario))
            except sqlite3.Error as e:
                log_error(f"Erro ao buscar veiculo : {e}")
        return veiculos
    
    def buscar_marca_por_id(self,id:int):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM Marca WHERE id=?",(id,))
                row = cursor.fetchone()
                if row:
                    id,nome,sigla = row
                    return Marca(id,nome,sigla)
            except sqlite3.Error as e:
                log_error(f"erro ao buscar marca por id: {e}")
        return None

    def buscar_pessoa_por_cpf(self,cpf:int):
        if self.conn:
            try:
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM Pessoa WHERE cpf=?",(cpf,))
                row = cursor.fetchone()
                if row:
                    cpf,nome,nascimento,oculos = row
                    return Pessoa(cpf,nome,nascimento,oculos)
            except sqlite3.Error as e:
                log_error(f"erro ao buscar pessoa por cpf: {e}")
        return None

    def fechar_conexao(self):
        if self.conn:
            limpar_log()
            self.conn.close()
            self.conn = None

