import Contato
class ControleContatos:
    def __init__(self,contato: Contato):
        self.listacontatos = [{"nome":contato.nome,"sobrenome":contato.sobrenome,"telefone":contato.telefone,"email":contato.email}]

        