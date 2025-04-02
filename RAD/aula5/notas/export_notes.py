from Aluno import *
import os

def export_notes(turma):

    choose = input("\nX para exportar notas ou A para adicionar aluno: ").lower()
    if choose == "x":
        path = 'notas.txt'
        if not os.path.exists(path):
            for aluno in turma:
                with open(path,'a',encoding='utf-8') as file:
                    file.writelines(f"Aluno: {aluno}\n")
                
            print("Dados da turma exportados para notas.txt")
            return 0
        else:
            print(FileExistsError , f"arquivo {path} já existente")
    
    elif choose == "a":
        return 0

    else: print("\nOpção inválida")
            