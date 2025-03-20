'''Permita que a Pessoa tenha mais de um endereço e imprima todos.'''
from src.classes.Locations import *
from src.modules.checker import verify
from src.RAD.aula3.manip import create_file

#iniciando atributos com qualquer conteúdo exclusivo para melhorar debug
people = People("voidex","voidex","voidex")
program = "addresses"

def endereco():
    people.location.street = input("\nRua: ")
    people.location.city = input("\nCidade: ")

def make_lista():

    endereco()
    region = f"{people.location.street}, {people.location.city}" 
    people.add_location(region)
    verify("Adicionar mais um endereço ? S/N: ",make_lista,"opção inválida")

def Pg_enderecos():

    print("\nExecutando Programa de endereços... ")
    people.name = input("\nNome do(a) morador(a): ")
    people.age = input("\nidade do(a) morador(a): ")
    make_lista()
    create_file(program,people.list)
    