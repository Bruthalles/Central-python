from datetime import date
from Pessoa import Pessoa
from Marca import Marca
from Veiculo import Veiculo
from banco import BancoDeDados

if __name__ == "__main__":

    banco = BancoDeDados()

    banco.conectar()
    banco.criar_table()
    pessoa1 = Pessoa(cpf=12222222,nome="Raphael",nascimento="1984-07-27",oculos=True)
    banco.inserir_pessoa(pessoa1)

    print("\nMarcas:")
    for marca in banco.buscar_todas_marcas():
        print(marca)
    
    print("\nVeiculos:")
    for veiculo in banco.buscar_todos_veiculos():
        print(veiculo)
    
    banco.fechar_conexao()