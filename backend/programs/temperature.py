from backend.classes.ConversorTemp import *
from backend.modules.timer import tm

def Pg_temp():
    print(f"\nExecutando Programa Conversor de temperatura... ")
    tm(1.0)

    choose = input(f"\n Escolha valor para converter, 'C' para Celsius, 'F' para Fahrenheit , 'K' para Kelvin ou 'R' para Rankine: ").upper()
    if (choose == "C"):
        twoose = input("\nAgora escolha F , K ou R: ").upper()
        if(twoose == "F"):
            celsius = float(input("\nDigite o grau em Celsius para retornar Fahrenheit: "))
            print(ConversorTemp.celsius_to_fahrenheit(celsius))
        elif (twoose == "K"):
            celsius = float(input("\nDigite o grau em Celsius para retornar Kelvin: "))
            print(ConversorTemp.celsius_to_kelvin(celsius))
        elif(twoose == 'R'):
            celsius = float(input("\nDigite o grau em Celsius para retornar Rankine: "))
            print(ConversorTemp.celsius_to_rankine(celsius))
        else:
            print("\nopção inválida")
            tm(1.4)
            return 0

    elif(choose == "F"):
        twoose = input("\n Agora escolha C , K ou R: ").upper()
        if (twoose == "C"):
            fahr = float(input("\nDigite o grau em Fahrenheit para retornar Celsius: "))
            print(ConversorTemp.fahrenheit_to_celsius(fahr))
        elif(twoose == "K"):
            fahr = float(input("\nDigite o grau em Fahrenheit para retornar Kelvin: "))
            print(ConversorTemp.fahrenheit_to_kelvin(fahr))
        elif(twoose == "R"):
            fahr = float(input("\nDigite o grau em Fahrenheit para retornar Rankine: "))
            print(ConversorTemp.fahrenheint_to_rankine(fahr))
        else:
            print("\nopção inválida")
            tm(1.4)
            return 0

    elif(choose == "K"):
        twoose = input("\nAgora escolha C , F ou R: ").upper()
        if(twoose == "C"):
            kelvin = float(input("\nDigite o grau em Kelvin para retornar Celsius: "))
            print(ConversorTemp.kevil_to_celsius(kelvin))
        elif(twoose == "F"):
            kelvin = float(input("\nDigite o grau em Kelvin para retornar Fahrenheit: "))
            print(ConversorTemp.kelvin_to_fahrenheit(kelvin))
        elif(twoose == "R"):
            kelvin = float(input("\nDigite o grau em Kelvin para retornar Rankine: "))
            print(ConversorTemp.kelvin_to_rankine(kelvin))
        else:
            print("\nopção inválida")
            tm(1.4)
            return 0
    elif(choose == "R"):
        twoose = input("\nAgora escolha C , F ou K: ").upper()
        if(twoose == "C"):
            rankine = float(input("\nDigite o grau em Rankine para retornar Celsius: "))
            print(ConversorTemp.rankine_to_celsius(rankine))
        elif(twoose == "F"):
            rankine = float(input("\nDigite o grau em Rankine para retornar Fahrenheit: "))
            print(ConversorTemp.rankine_to_fahrenheit(rankine))
        elif(twoose == "K"):
            rankine = float(input("\nDigite o grau em Rankine para retornar Kelvin: "))
            print(ConversorTemp.rankine_to_kelvin(rankine))
        else:
            print("\nopção inválida")
            tm(1.4)
            return 0
    else:
        print("\nopção inválida")
        tm(1.4)
        return 0