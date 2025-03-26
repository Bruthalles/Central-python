import re

'''texto = "Nossa primeira aula manipulando string."
print(texto[0:20:2])
print(len(texto))
print(texto.count("a"))
print(texto.count("a",5,36))
print(texto.find("aula"))
print(texto.find("Arroz"))
print("String"in texto)
print("a"in texto)

novo_texto = texto.replace("manipulando","trabalhando com")
print(novo_texto)

print(texto.startswith("Nossa"))
print(texto.startswith("aula"))
print(texto.endswith("aula"))
print(texto.endswith("."))

print(texto.lower())
print(texto.upper())
print(texto.capitalize())
print(texto.title())
print(texto.swapcase())'''

'''nome = str(input("digite nome: "))
print(f"Olá,{nome}!")
print(f"Olá,{nome.strip()}!")
#rstrip() limpa espaço na direita
#lstrip() limpa espaço na esquerda

print(texto)
print(f"texto cortado: {texto.split()}")
print(f"espaçio inserido: {''.join(texto)}")
print(f"texto cortado: {texto.split()}")
print(f"texto cortado e com espaço: {''.join(texto.split())}")

def get_coxinhas(*pedidos):
    return [f'{pedido} coxinhas'for pedido in pedidos]

salgados_return = get_coxinhas(4,6,8)
print("usando return")
print(salgados_return)

def get_joelho(*pedidos):
    for pedido in pedidos:
        yield f"{pedido} joelho(s)"

print("\nusando yield")
for salgado in get_joelho(4,6,8):
    print(salgado)'''

'''texto = "o numero de telefone é (123) 456-7890"
padrao = r'\(\d{3}\) \d{3}-\d{3}'

resultado = re.search(padrao,texto)

if resultado:
    numero_telefone = resultado.group()
    print("numero de telefone encontrado",numero_telefone)
else: print("numero nao encontrado")

texto = "meu email é exemplo@gmail.com"
padrao = r'\b\w+@+\w+\.\w+b'

novotexto = re.sub(padrao,"[email oculto]",texto)
print(novotexto)'''

def verify_email(email):
    pattern = r"^\b\w+@\w+\.\w+\b$"
    if re.fullmatch(pattern,email):
        print(f"\nEmail: '{email}' válido!")
    else:
        print("\nemail invalido")