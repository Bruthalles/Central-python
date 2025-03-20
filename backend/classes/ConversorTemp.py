'''Exercício:
Crie uma classe ConversorTemperatura com:

Um método estático celsius_para_fahrenheit(celsius).
Um método estático fahrenheit_para_celsius(fahrenheit).
Desafio extra:
Chame esses métodos sem instanciar a classe.'''
class ConversorTemp:
    @staticmethod 
    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 1.8) + 32
        return f"\n{celsius}°C = {fahrenheit}°F"
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit -32) *5 / 9
        return f"\n{round(fahrenheit,2)}°F = {round(celsius,2)}°C"