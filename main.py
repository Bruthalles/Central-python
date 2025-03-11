import boolear
from classes.Carro import Carro
from classes import Cadastro
from classes import ContaBancaria

usr = Cadastro.Usuario()
count = ContaBancaria.Contabancaria(0,0)

def menu():
    print(f"=======Bem-vindo, {usr.name}=======")
    print("\nDigite 1 para ver saldo |")
    print("\nDigite 2 para depositar |")
    result = int(input("\nDigite 3 para sacar: "))

    if(result== 1):
        count.show_balance()
        menu()

    elif(result==2):
        valor = input("\nQuanto irá depositar? ")
        count.fill(valor)
        menu()

    elif(result==3):
        valor = input("\nDigite valor para saque: ")
        count.empty(valor)
        menu()

    else: 
        print("\nOPÇÃO INDISPONÍVEL!")
        menu()

def login():

    check_name = input("\nInsira nome de usuário: ")
    check_passw = input("\nInsira sua senha: ")

    if(check_name == usr.name and check_passw == usr.passw):
        menu()

    else: print("\nNOME DE USUÁRIO OU SENHA INCORRETOS")


if __name__ == "__main__":
    if (usr.name == None):
        usr.name = input("\nCadastre um nome de usuário para entrar na conta: ")

    if(usr.passw == None):
        usr.passw = input("\nCadastre sua senha para passar: ")
        login()

    
    else:
        login()

    
    

        