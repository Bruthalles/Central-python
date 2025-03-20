import os

#path prepared to future uses
path = 'dados.txt'
abspath = 'home/thalles/thapython/'+path

#function to clean file
def clean():
    option = input("\nwould you like to clean the file? S/N: ")
    option = option.upper()

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
    with open(path,'w') as file:
        file.writelines(["ana","\nmaria"])
        print(file)

write()
read()
clean()