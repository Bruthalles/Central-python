'''Exercício:
Crie uma classe Carro com os atributos marca, modelo e ano. Adicione um método exibir_detalhes() que imprime essas informações.

Desafio extra:
Crie um objeto da classe Carro e chame o método exibir_detalhes().'''

class Car:
    
    def __init__(self,marca= "nulo",modelo="nulo",ano=0):
        self.marca = marca 
        self.modelo = modelo
        self.ano = ano

    def set_info(self):
        self.marca = input("Marca: ")
        self.modelo = input("Modelo: ")
        self.ano = input("Ano: ")

    def show_info(self):
        print("\ninformaçoes do seu carro:")
        print(f"{self.marca} {self.modelo} {self.ano}")