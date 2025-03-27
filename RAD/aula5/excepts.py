try:
    f = open ('RAD\aula5\nomes.txt')
    s = f.readline()
    i = int(s.strip())

except FileNotFoundError as ffe:
    print("arquivo nao encontrado")
except IOError as io:
    print("erro na abertura do arquivo")
except ValueError as val:
    print("formato invalido encontrado no arquivo")
except Exception as e:
    print(f"\nErro inesperado: {e}")
    raise