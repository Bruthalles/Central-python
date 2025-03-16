'''Exercício:
Crie uma classe Pessoa com nome e idade. Depois, crie uma classe Endereco com rua e cidade.
A classe Pessoa deve ter um atributo endereco que recebe um objeto da classe Endereco.

Desafio extra:
Permita que a Pessoa tenha mais de um endereço e imprima todos.'''
        
class Location():
    def __init__(self,street,city):
        self.street = street
        self.city = city

obj_Location = Location("","")

class People():
    def __init__(self,name,age,location):
        location = obj_Location
        self.name = name
        self.age = age
        self.location = obj_Location
        self.list = []
    
    def add_location(self,list:str):
        self.list.append(list)
        print("\nNovo endereço adicionado!")
        print("\nAgora sua lista de endereços é:")
        print(list())