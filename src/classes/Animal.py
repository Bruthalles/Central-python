'''Crie uma classe Animal com um método fazer_som(). Depois, crie duas classes Cachorro e Gato que herdam de Animal e sobrescrevem fazer_som() para retornar "Au Au!" e "Miau!", respectivamente.

Desafio extra:
Crie uma lista de animais (cães e gatos misturados) e percorra a lista chamando fazer_som().'''

#definindo tudo o que será exportado
__all__ = ["Cat","Dog"]

class Animal:
    
    def __init__(self,name):
        self.name = name

    def fazer_som(str):
        print(str)
        return 0 

class Cat(Animal):
    pass

class Dog(Animal):
    pass