from backend.classes.Animal import Cat,Dog
from backend.modules.timer import tm
#iniciando com string exclusiva para debug
cat = Cat("voidex")
dog = Dog("voidex")

def catordog():
    pet = input("\nCat or dog? ").lower()
    if(pet == "cat"):
        return "\n MIAAAAAAAAAAAAAAAAAAU"
        
    elif(pet == "dog"):
        return "\nAUUUUUUUUUUUUUUUUUUUU"
    else:
        return(f"Por acaso você não sabe escrever ou só tá me testando?\nIsso aqui não é bagunça, ou você me obedece ou cai fora >:(")
        
    
def Pg_animals():
    print("\nExecutando Programa de animais... ")
    tm(1.0)

    Cat.fazer_som(catordog())
    