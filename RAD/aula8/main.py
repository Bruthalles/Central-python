from datetime import date
from Pessoa import Pessoa
from Marca import Marca
from Veiculo import Veiculo

pessoa1 = Pessoa(cpf=123456789,nome='josé',nascimento=date(1984,7,26),oculos=True)

marca1 = Marca(id=1,nome='Fiat',sigla='FIA')

veiculo1 = Veiculo('A23B1',"cinza",pessoa1,marca1)

print(veiculo1)