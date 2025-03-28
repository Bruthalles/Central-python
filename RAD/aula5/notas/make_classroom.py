def make_classroom(name,nota,turma):

    state_loop = True

    while state_loop:
        name = input("\nDigite nome do aluno ou X para encerrar: ").lower()

        if name == "x":
            state_loop = False
        else: 
            turma = turma.append(name)
            nota = int(input(f"\n Digite nota do(a) {name}: "))
            print(turma)
            print(f"\n tamanho da turma: {len(turma)} alunos")
