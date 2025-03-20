from src.programs.car import Pg_Car
from src.programs.bank import Pg_bank
from src.programs.animals import Pg_animals
from src.programs.temperature import Pg_temp
from src.programs.elocations import Pg_enderecos

def Choose_pg():
    print(f"\nLista de programas: ")
    print(f"\n Nº1: Executar car.py |")
    print(f"\n Nº2: Executar bank.py |")
    print(f"\n Nº3: Executar animals.py |")
    print(f"\n Nº4: Executar temperature.py |")
    print(f"\n Nº5: Executar enderecos.py |")
    choose = int(input(f"\n Escolha qual programa executar, ou 6 para encerrar: "))

    if(choose== 1):
        Pg_Car()
        Choose_pg()
    elif(choose== 2):
        Pg_bank()
        Choose_pg()
    elif(choose== 3):
        Pg_animals()
        Choose_pg()
    elif(choose== 4):
        Pg_temp()
        Choose_pg()
    elif(choose== 5):
        Pg_enderecos()
        Choose_pg()
    elif(choose==6):
        return 0
    else:
        print("Programa inexistente!")
        Choose_pg()
   
if __name__ == "__main__":

    Choose_pg()
    