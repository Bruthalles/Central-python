from backend.classes.ConversorTemp import *
from backend.modules.timer import tm

def Pg_temp():
    print(f"\nExecutando Programa Conversor de temperatura... ")
    tm(1.0)

    choose = input(f"\n Escolha valor para converter, 'C' para Celsius, 'K' para Kelvin ou 'F' para Fahrenheit: ").upper()
    if (choose == "C"):
        twoose = input("\nAgora escolha K ou F: ").upper()
        if (twoose == "K"):
            celsius = float(input("\nDigite o grau em celsius para retornar em Kelvin: "))
            tm(1.5)
            print(ConversorTemp.celsius_to_kelvin(celsius))
            tm(1.2)
        elif(twoose == "F"):
            celsius = float(input("\nDigite o grau em celsius para retornar em Fahrenheit: "))
            tm(1.5)
            print(ConversorTemp.celsius_to_fahrenheit(celsius))
            tm(1.2)
        else:
            print("\nopção inválida")
            tm(1.4)
            return 0

    elif(choose == "F"):
        twoose = input("\n Agora escolha C ou K: ").upper()
        if (twoose == "C"):
            fahr = float(input("\nDigite o grau em fahrenheit para retornar celsius: "))
            tm(1.5)
            print(ConversorTemp.fahrenheit_to_celsius(fahr))
            tm(1.2)
        elif(twoose == "K"):
            fahr = float(input("\nDigite o grau em fahrenheit para retornar em kelvin: "))
            tm(1.5)
            print(ConversorTemp.fahrenheit_to_kelvin(fahr))
            tm(1.2)
        else:
            print("\nopção inválida")
            tm(1.4)
            return 0

    elif(choose == "K"):
        twoose = input("\nAgora escolha C ou f: ").upper()
        if(twoose == "C"):
            kelvin = float(input("\nDigite o grau em kelvin para retornar em celsius: "))
            tm(1.5)
            print(ConversorTemp.kevil_to_celsius(kelvin))
            tm(1.2)
        elif(twoose == "F"):
            kelvin = float(input("\nDigite o grau em kelvin para retornar em fahrenheit: "))
            tm(1.5)
            print(ConversorTemp.kelvin_to_fahrenheit(kelvin))
            tm(1.2)
        else:
            print("\nopção inválida")
            tm(1.4)
            return 0
    else:
        print("\nopção inválida")
        tm(1.4)
        return 0