from Aluno import *
import os,time
from up_down_timer import up_down_timer
tm = time.sleep
def export_notes(turma):

    choose = input("\nX para exportar notas ou A para adicionar aluno: ").lower()
    if choose == "x":
        path = 'RAD/ex.exportar_notas/notas.txt'
        if not os.path.exists(path):

            with open(path,'w',encoding='utf-8')as f:
                f.write('')
            tm(5.0)
            for aluno in turma:
                with open(path,'a',encoding='utf-8') as file:
                    file.write(f"Aluno: {aluno.nome}. Nota: {aluno.nota}\n")
                
            print("Dados da turma exportados para notas.txt")
            return 0
        else:
            print(FileExistsError , f"arquivo {path} já existente")
            twoose = int(input("\nDigite 1 para adicionar mesmo assim ou digite 2 para sobrescrever: "))
            if twoose == 1:
                tm(5)
                for aluno in turma:
                    with open(path,'a',encoding='utf-8') as file:
                        file.write(f"Aluno: {aluno.nome}. Nota: {aluno.nota}\n")
            
                print("novo aluno adicionado à turma")
                return 0
            elif twoose ==2:
                print("ARQUIVO  notas.txt SERÁ SOBRESCREVIDO EM 10 SEGUNDOS:")
                up_down_timer()
                tm(5)

                with open(path,'w') as w:
                    w.write('')
                for aluno in turma:
                    with open(path,'a',encoding='utf-8') as file:
                        file.write(f"Aluno: {aluno.nome}. Nota: {aluno.nota}\n")
            
                print("notas.txt sobrescrevido com a nova turma")
                return 0
            else: print("\nOpção invalida")
    
    elif choose == "a":
        return 0

    else: print("\nOpção inválida")
            