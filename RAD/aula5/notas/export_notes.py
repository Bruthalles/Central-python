from Aluno import *
import os

def export_notes(nome,nota,turma):
   
    choose = input("\nX para exportar notas ou A para adicionar aluno: ").lower()
    if choose == "x":
        path = "notas.txt"
        
        if not os.path.exists(path):
            while len(turma):
                with open(path,'w',encoding='utf-8') as file:
                    file.writelines(f"Aluno: {nome.capitalize()}, Nota: {nota}")
                    file.writelines("\n")
            print("Dados da turma exportados para notas.txt")
            print(nome,nota)
        else:
            print(FileExistsError , "arquivo já existente")

    elif choose == "a":
        Aluno.make_classroom(nome,nota,turma)

    else: print("\nOpção inválida")
            