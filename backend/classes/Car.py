'''Exercício:
Crie uma classe Carro com os atributos marca, modelo e ano. Adicione um método exibir_detalhes() que imprime essas informações.

Desafio extra:
Crie um objeto da classe Carro e chame o método exibir_detalhes().'''
class Car:
    
    def __init__(self,marca= "nulo",modelo="nulo",ano=0):
        self.marca = marca.capitalize()
        self.modelo = modelo.capitalize()
        self.ano = ano
        self.cars = []

    def set_info(self):
        self.marca = input("Marca: ").capitalize()
        self.modelo = input("Modelo: ").capitalize()
        self.ano = input("Ano: ")
        
    def add_car(self,objcar):
        self.cars.append(objcar)
        print("\nSua garagem:")
        for i in self.cars:
            print(f"\n{i}")
        return 0
    
    def to_dict(self):
        return{
            "Marca": self.marca,
            "Modelo": self.modelo,
            "Ano": self.ano
        }