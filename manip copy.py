caminho = 'dados.txt'

def ex01():

    
    arquivo = open(caminho,'w')     
    arquivo.write('thalles')
    
    arquivo = open(caminho,'r')
    print(f"conteudo do arquivo: {arquivo.readline}")
    print("teste")
    arquivo.close()

def ex02():

    arquivo = open(caminho,'r')
    
    linha1= arquivo.readline()
    print(f"linha1: {linha1}")
    linha2 = arquivo.readline()
    print(f"linha2: {linha2}")
    arquivo.close()

def ex3():
    arquivo = open(caminho,'w')
    arquivo.write("\n a")
    print(arquivo)
    print("teste")
    arquivo.close()

ex01()
ex3()
ex02()