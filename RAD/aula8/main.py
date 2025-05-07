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
    pessoa2 = Pessoa(cpf=43210987,nome="Gojira",nascimento="2005-02-04",oculos=True)
    banco.inserir_pessoa(pessoa2)

    marca1 = Marca(id=1,nome="fiat",sigla='FIA')
    banco.inserir_marca(marca1)
    marca2 = Marca(id=2,nome='chevrolet',sigla='CHV')

    carro1 = Veiculo(placa="12a4re",cor="prata",marca=marca1,proprietario=pessoa1)
    banco.inserir_veiculo(carro1)
    carro2 = Veiculo(placa='LVA11452',cor="azul",marca=marca2,proprietario=pessoa2)

    print("\nPessoas:")
    for pessoa in banco.buscar_todas_pessoas():
        print(pessoa)

    print("\nMarcas:")
    for marca in banco.buscar_todas_marcas():
        print(marca)
    
    print("\nVeiculos:")
    for veiculo in banco.buscar_todos_veiculos():
        print(veiculo)

    
    pessoa1 = Pessoa(cpf=123456789,nome="Michelangelo",nascimento="1502",oculos=False)
    banco.atualizar_pessoa(pessoa1)

    banco.apagar_veiculo()
    
    banco.fechar_conexao()