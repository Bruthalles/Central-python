from classes.Car import Car
from timer import tm
from checker import verify

car = Car()

def make_garage():
    car.set_info()
    garage = f"{car.marca}|{car.modelo}|{car.ano}"
    car.add_car(garage)
    verify("Adicionar novo carro ? S/N: ",make_garage,"opção inválida!")
    return 0

def Pg_Car():
    print("\nExecutando Programa de carros... ")
    tm(1.0)
    make_garage()
    tm(1.0)