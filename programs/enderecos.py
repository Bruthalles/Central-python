from classes.Relationship import *

def Pg_enderecos():
    print("\nExecutando Programa de endereços... ")
    location = Location("nulo","nulo")
    people = People("nulo","nulo","nulo")


    people.name = "joaco"
    people.age = "392"
    people.location = location("rua b","rj")

    print(f"\n{people.name}\n{people.age}\n{people.location}")