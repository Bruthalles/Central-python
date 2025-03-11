""" Crie uma classe ContaBancaria com:

Um atributo privado saldo.
Métodos depositar(valor) e sacar(valor), verificando se há saldo suficiente.
Desafio extra:
Adicione um método exibir_saldo() que exibe o saldo apenas se for chamado de dentro da classe. """

class Contabancaria:
    def __init__(self,balance, valor):
        self.__balance = balance
        self.valor = valor

    def fill(self,valor):

        if(valor >0):
            self.__balance += valor
            print("\nR${valor} depositado!")

        else: print("\nValor inválido para depósito")

    def empty(self,valor):
        if(0<valor<=self.__balance):
            self.__balance -= valor
            print(f"\nSaque de R${valor} efetuado!")

        else: print("\nSaldo insuficiente ou inválido")

    def show_balance(self):
        print(f"R${self.__balance}")