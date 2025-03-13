'''Exercício:
Crie uma classe ContaBancaria com:

Um atributo privado saldo.
Métodos depositar(valor) e sacar(valor), verificando se há saldo suficiente.
Desafio extra:
Adicione um método exibir_saldo() que exibe o saldo apenas se for chamado de dentro da classe'''

class Usuario():
     name = None
     passw = None

class Contabancaria:
    def __init__(self,balance, valor):
        self.__balance = float(balance)
        self.valor = float(valor)

    def fill(self,valor):

        if(float(valor) >0):
            self.__balance += float(valor)
            print(f"\nR${valor} depositado!")
        else: print("\nValor inválido para depósito")

    def empty(self,valor):

        if(0<float(valor)<=self.__balance):
            self.__balance -= float(valor)
            print(f"\nSaque de R${valor} efetuado!")
        else: print("\nSaldo insuficiente ou inválido")

    def show_balance(self):
        print(f"\nSeu saldo atual é: R${self.__balance}")