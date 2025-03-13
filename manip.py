caminho = 'dados.txt'

def ex01():

    
    arquivo = open(caminho,'w')     
    arquivo.write('thalles')
    arquivo.close()

    arquivo = open(caminho,'r')
    print(f"conteudo do arquivo: {arquivo.readline}")
    arquivo.close()

def ex02():
    arquivo = open(caminho,'r')
    linha1= arquivo.readline()
    print(f"linha1: {linha1}")
    linha2 = arquivo.readline()
    print(f"linha2: {linha2}")
    arquivo.close()
    

ex01()
ex02()