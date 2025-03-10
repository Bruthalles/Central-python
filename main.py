import boolear
from classes.Carro import Carro
from classes import Cadastro

cliente1 = Cadastro.Cadastro()
 
carro = Carro()


if __name__ == "__main__":
    
    carro.set_info()
    carro.show_info()

        