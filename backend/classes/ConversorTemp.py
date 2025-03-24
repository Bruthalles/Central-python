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
        return f"\n{celsius}°C = {kelvin}°K"
    
    @staticmethod
    def kevil_to_celsius(kelvin):
        celsius = kelvin - 273.15
        return f"\n{kelvin}°K = {celsius}°C"
    
    @staticmethod 
    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 1.8) + 32
        return f"\n{celsius}°C = {fahrenheit}°F"
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit -32) * 5 / 9
        return f"\n{round(fahrenheit,2)}°F = {round(celsius,2)}°C"
    
    @staticmethod
    def fahrenheit_to_kelvin(fahr):
        kelvin = (fahr +459.67) * 5 / 9
        return f"\n{fahr}°F = {round(kelvin,4)}°K"
    
    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        fahr = kelvin * 9 / 5 - 459.67
        return f"\n{kelvin}°K = {round(fahr,3)}°F"