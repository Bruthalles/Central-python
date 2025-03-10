import boolear
from classes import *

cliente1 = Cadastro.Cadastro()

if __name__ == "__main__":
    cliente1.nome = input("\nDigite nome do cliente: ")
    cliente1.idade = input("\nDigite idade do cliente: ")
    cliente1.endereco = input("\nDigite endereço do cliente: ")

        