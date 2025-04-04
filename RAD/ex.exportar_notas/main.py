'''voce é um professor e deseja guardar registro de notas dos alunos. pode usar um arquivo de texto para armazenar as notas de cada aluno'''
from Aluno import *
from export_notes import *

aluno = Aluno()
if __name__ == '__main__':
    state_loop = True

    while state_loop:
        choose = input("\nDigite A para adicionar aluno ou C para cancelar: ").lower()
        #só para se turma receber pelo menos um aluno
        if choose == "c" and len(aluno.turma) >0:
            state_loop = False
        else: 
            aluno.make_classroom()