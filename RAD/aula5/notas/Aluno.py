import os
class Aluno:
    def __init__(self,nome='',nota='',turma='') -> str:
        self.nome = nome
        self.nota = nota
        self.turma =[]

    def make_classroom(self,nome,nota,turma):
        
        self.nome = input("\nDigite nome do aluno: ")
        self.nota = int(input(f"\nDigite nota do aluno: "))
        self.turma.append(nota)
        #debugs
        print(self.turma)
        print(nome,nota)
        print(f"\ntamanho da turma: {len(self.turma)} alunos")
        choose = input("\nX para exportar notas ou A para adicionar aluno: ").lower()
        if choose == "x":
            path = 'notas.txt'
            if not os.path.exists(path):
                with open(path,'w',encoding='utf-8') as file:
                    file.writelines(f"Aluno: {self.nome.capitalize()}, Nota: {self.nota}")
                    file.writelines("\n")
            else:
                print(FileExistsError , "arquivo já existente")
        
    
        