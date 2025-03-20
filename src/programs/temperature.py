from src.classes.ConversorTemp import *
from src.modules.timer import tm
program = "conversion"
def Pg_temp():
    print(f"\nExecutando Programa Conversor de temperatura... ")
    tm(1.0)

    choose = input(f"\n Escolha 'C' para Celsius ou 'F' para Fahrenheit: ").upper()
    if (choose == "C"):
        celsius = float(input("\nDigite o grau em celsius para retornar fahrenheit: "))
        tm(1.5)
        print(ConversorTemp.celsius_to_fahrenheit(celsius))
        tm(1.2)
    elif(choose == "F"):
        fahr = float(input("\nDigite o grau em fahrenheit para retornar celsius: "))
        tm(1.5)
        print(ConversorTemp.fahrenheit_to_celsius(fahr))
        tm(1.2)
    else:
        print("\nopção inválida")
        tm(1.4)
        return 0