import getpass
from classes.ContaBancaria import *

usr = Usuario()
count = Contabancaria(0,0)
program = "account"
def option():
    result = int(input("\nEscolha uma ação: "))

    if(result== 1):
        count.show_balance()
        option()

    elif(result==2):
        valor = input("\nQuanto irá depositar? ")
        count.fill(valor)
        option()

    elif(result==3):
        check_pass = getpass.getpass("\ninsira sua senha para confirmar: ")
        if(check_pass == usr.passw):
            valor = input("\nDigite valor para saque: ")
            count.empty(valor)
            option()
        else:
            print("\nSenha incorreta!")
            option()

    elif(result==4):
        return 0
    else: 
        print("\nOPÇÃO INDISPONÍVEL!")
        option()

def menu():
    
    print("\nDigite 1 para ver saldo |")
    print("\nDigite 2 para depositar |")
    print("\nDigite 3 para resgatar  |")
    print("\nDigite 4 para sair      |")
    option()

def login():

    check_name = input("\nInsira nome de usuário: ").capitalize()
    check_passw = getpass.getpass("\nInsira sua senha: ")

    if(check_name == usr.name and check_passw == usr.passw):
        print(f"\n=======Bem-vindo, {usr.name}=======")
        menu()

    else: print("\nNOME DE USUÁRIO OU SENHA INCORRETOS")

def Pg_bank():

    print("\nExecutando Programa do banco... ")
    if (usr.name == None):
        usr.name = input("\nCadastre um nome de usuário para entrar na conta: ").capitalize()

    if(usr.passw == None):
        usr.passw = getpass.getpass("\nCadastre sua senha para passar: ")
        login()
    else:
        login()