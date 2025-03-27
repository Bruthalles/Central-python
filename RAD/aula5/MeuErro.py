
class MeuErro(Exception):
    pass

def dividir(numerador, denominador):
    if denominador == 0:
        raise MeuErro("Divisão por zero não épermitido!")
    return numerador / denominador 

try:
    resultado = dividir(10,0)
    print("Resultado:", resultado)
except MeuErro as erro:
    print("Ocorreu um error:", erro)
