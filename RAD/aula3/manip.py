import os
#path prepared to future uses
path = 'dados.txt'
abspath = 'home/thalles/thapython/'+path

#function to clean file
def clean():
    option = input(f"\nwould you like to clean {path}? S/N: ").upper()

    if(option == 'S'):
        with open(path,'w',encoding='utf-8') as file:
            file.write("")
            print("file content cleaned!")
        with open(path,'r',encoding='utf-8')as file:
            linha1 = file.readline() 
            print(f"linha1: {linha1}")
            linha2 = file.readline()
            print(f"linha2: {linha2}")

def write():
    if os.path.exists(path):
        print("arquivo existente")
    else:
        with open(path,'w',encoding='utf-8') as file:
            reply = input("type something to save: ")
            file.writelines(reply)
            reply = input("type something to save: ")
            file.writelines(f"\n{reply}")

            file = open(path,'r')
            print(f"content of file: {file.read()}")

def read():

    with open(path,'r') as file:
        linha1 = file.readline() 
        print(f"linha1: {linha1}")
        linha2 = file.readline()
        print(f"linha2: {linha2}")
    
#function to add many lines of once
def add():
    with open('extra.txt','x') as file:
        file.writelines(["ana","\nmaria"])
        print(file.read())

def create_file(program="",content=""):
    #length = len(content)
    choose = input(f"\nType 'S' to create a file about your {program}, Anything else to skip: ").upper()
    if(choose == "S"):
        name = input(f"Which name do you like to put? ")
        if os.path.exists(name):
            print("\nThis file  exists already")
            create_file(program,content)
        
        with open(f"{name}.txt",'x',encoding='utf-8') as file:
            for i in len(content):
                file.writelines(f"\n({content[i]})")
    else: return 0
