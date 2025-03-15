'''Exercício:
Crie uma classe Pessoa com nome e idade. Depois, crie uma classe Endereco com rua e cidade.
A classe Pessoa deve ter um atributo endereco que recebe um objeto da classe Endereco.

Desafio extra:
Permita que a Pessoa tenha mais de um endereço e imprima todos.'''
        
class Location():
    def __init__(self,street,city):
        self.street = street
        self.city = city


class People():
    def __init__(self,name,age,location):
        self.name = name
        self.age = age
        self.location = location.Location("","")
        