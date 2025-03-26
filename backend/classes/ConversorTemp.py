'''Exercício:
Crie uma classe ConversorTemperatura com:

Um método estático celsius_para_fahrenheit(celsius).
Um método estático fahrenheit_para_celsius(fahrenheit).
Desafio extra:
Chame esses métodos sem instanciar a classe.'''
class ConversorTemp:

    @staticmethod
    def celsius_to_kelvin(celsius):
        kelvin = celsius + 273.15
        return f"\n{round(celsius,2)}°C = {round(kelvin,2)}°K"
    
    @staticmethod
    def kevil_to_celsius(kelvin):
        celsius = kelvin - 273.15
        return f"\n{round(kelvin,2)}°K = {round(celsius,2)}°C"
    
    @staticmethod 
    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 1.8) + 32
        return f"\n{round(celsius,2)}°C = {round(fahrenheit,2)}°F"
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit -32) * 5 / 9
        return f"\n{round(fahrenheit,2)}°F = {round(celsius,2)}°C"
    
    @staticmethod
    def fahrenheit_to_kelvin(fahr):
        kelvin = (fahr +459.67) * 5 / 9
        return f"\n{round(fahr,2)}°F = {round(kelvin,2)}°K"
    
    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        fahr = kelvin * 9 / 5 - 459.67
        return f"\n{round(kelvin,2)}°K = {round(fahr,2)}°F"
    
    @staticmethod
    def celsius_to_rankine(celsius):
        rankine = (celsius + 273.15) * 9 / 5 
        return f"\n{round(celsius,2)}°C = {round(rankine,2)}°R"
    
    @staticmethod
    def rankine_to_celsius(rankine):
        celsius = (rankine - 491.76) * 5 / 9
        return f"\n{round(rankine,2)}°R = {round(celsius,2)}°C" 
    
    @staticmethod
    def fahrenheint_to_rankine(fahr):
        rankine = fahr + 459.67
        return f"\n{round(fahr,2)}°F = {round(rankine,2)}°R"

    @staticmethod
    def rankine_to_fahrenheit(rankine):
        fahr = rankine - 459.67
        return f"\n{round(rankine,2)}°R = {round(fahr,2)}°F"
    
    @staticmethod
    def kelvin_to_rankine(kelvin):
        rankine = kelvin * 9 / 5
        return f"\n{round(kelvin,2)}°K = {round(rankine,2)}°R"

    @staticmethod
    def rankine_to_kelvin(rankine):
        kelvin = rankine * 5 / 9
        return f"\n{round(rankine,2)}°R = {round(kelvin,2)}°K"