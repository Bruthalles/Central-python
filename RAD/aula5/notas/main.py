'''voce é um professor e deseja guardar registro de notas dos alunos. pode usar um arquivo de texto para armazenar as notas de cada aluno'''
import os
from make_classroom import make_classroom
from Aluno import Aluno

aluno = Aluno()
if __name__ == '__main__':

    print(aluno.turma)
    make_classroom(aluno.nome,aluno.nota, aluno.turma)
    



        
