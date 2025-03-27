def loop_aluno(name,note,turma):
    name = input("\nDigite nome do aluno ou X para encerrar: ").lower()

    if name == "x":
        return 0
    else: 
        turma.append(name)
        turma = len(turma)
        note = input(f"\n Nota do aluno {name}: ")
        return note

