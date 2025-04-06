from export_notes import export_notes
class Aluno:
    def __init__(self,nome='',nota='',turma='') -> str:
        self.nome = nome
        self.nota = nota
        self.turma=[]

    def clear_turma(self):
        self.nome = None
        self.nota = None
        self.turma =[]

    def make_classroom(self):
        
        self.nome = input("\nDigite nome do aluno: ")
        self.nota = int(input(f"\nDigite nota do aluno: "))
        #adicionar condição da nota ser até 10 ->
        self.turma.append({'nome':self.nome.capitalize(),'nota':self.nota})

        # #debugs
        # print(self.turma)
        # print(nome,nota)
        # ###
        print(f"\ntamanho da turma: {len(self.turma)} alunos")
        export_notes(self.turma)
        self.clear_turma()
        return 0