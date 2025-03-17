from classes.Animal import Cat,Dog
from timer import tm


#iniciando com string exclusiva para debug
cat = Cat("voidex")
dog = Dog("voidex")

def catordog():

    pet = input("\n Cat or Dog ? ").lower()
   
    if(pet == "cat"):
        print(f"\nOlha o meme gritando miau:")
        tm(1.0)
        print(f"\nMIAAAAAAAAAAAAU")


    elif(pet == "dog"):
        print("\nAUUUUUUUUUUUU")
        tm(1.8)

        print("Baby, I'm preyin' on you tonight")
        tm(1.8)

        print("Hunt you down, eat you alive")
        tm(1.8)

        print("Just like animals, animals")
        tm(1.8)

        print("Like Animals-mals")
        tm(1.8)

    else:
        print(f"Por acaso você não sabe escrever ou só tá me testando?")
        tm(1.0)

        print(f"Isso aqui não é bagunça, ou você me obedece ou cai fora >:(")
    
def Pg_animals():
    print("\nExecutando Programa de animais... ")
    tm(1.0)

    Cat.fazer_som(catordog())
    