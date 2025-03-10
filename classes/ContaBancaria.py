""" Crie uma classe ContaBancaria com:

Um atributo privado saldo.
Métodos depositar(valor) e sacar(valor), verificando se há saldo suficiente.
Desafio extra:
Adicione um método exibir_saldo() que exibe o saldo apenas se for chamado de dentro da classe. """

class Contabancaria:
    balance = 0

    def fill(valor):
        balance = valor

    def empty(valor):
        balance = balance - valor

    def show_balance(balance):
        print(balance)