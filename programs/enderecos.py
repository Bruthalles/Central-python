'''Permita que a Pessoa tenha mais de um endereço e imprima todos.'''
#criar uma lista e colocar os endereços
#permitir o usuario escolher tamanho da lista

from classes.Relationship import *

#iniciando atributos com qualquer conteúdo exclusivo para melhorar debug
people = People("voidex","voidex","voidex")

def make_lista():

    choose = input("\nAdicionar mais um endereço ? S/N: ")
    choose.upper()
    if(choose == 'S'):
        
        people.location.street = input("\nNome da rua: ")
        people.location.city = input("\nCidade: ")
        people.add_location(people.location)
        

    else: return 0

def Pg_enderecos():

    print("\nExecutando Programa de endereços... ")
   
    people.name = input("\nNome do(a) morador(a): ")
    people.age = input("\nidade do(a) morador(a): ")
    people.location.street = input("\nNome da rua: ")
    people.location.city = input("\nCidade: ")

    make_lista()

    