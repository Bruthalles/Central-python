import Contato,os
from RAD.aula4.verify_email import verify_email

path = 'RAD/ex.agenda_contatos/contacts.txt'

class ControleContatos:
    def add_contact(self,contato: Contato):
        contato.nome = input("\nDigite seu nome: ")
        contato.sobrenome = input("\nDigite sobrenome: ")
        contato.email = input("\nDigite seu email:")
        email = verify_email(contato.email)

        while not email:
            contato.email = input("\nDigite seu email:")

        try:
            not os.path.exists(path)
            with open(path,'w')as p:
                p.write('')

        except FileExistsError as fee:
            print(f"\nArquivo já existente: {fee}")
        
        except FileNotFoundError as fnf:
            print(f"\n Arquivo não encontrado: {fnf}")

        except Exception:
            print("\nNão foi possível criar o arquivo")

        self.list_contact = [{"nome":contato.nome,"sobrenome":contato.sobrenome,"email":contato.email,"telefone":contato.telefone}]

        try:
            with open(path,'a',encoding='utf-8')as a:
                a.write(f"Nome: {contato.nome}. Sobrenome: {contato.sobrenome}. Email: {contato.email}. Telefone: {contato.telefone}")
        except Exception:
            print(Exception)
            
    def search_contact(self,contato:Contato):
        email = input("\nBusque contato pelo email: ")
        try:
            not os.path.exists(path)
            with open(path,'r')as p:
                p.readlines(email)
                #if email in path:

        except FileExistsError as fee:
            print(f"\nArquivo já existente: {fee}")
        
        except FileNotFoundError as fnf:
            print(f"\n Arquivo não encontrado: {fnf}")

        except Exception:
            print("\nNão foi possível criar o arquivo")