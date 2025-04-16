from dataclasses import dataclass
from Pessoa import Pessoa
from Marca import Marca

@dataclass
class Veiculo:
    placa: str
    cor: str
    marca : Marca
    proprietario : Pessoa