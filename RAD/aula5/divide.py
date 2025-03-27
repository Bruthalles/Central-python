def divide(x,y):
    try:
        resultado = x / y
    
    except ZeroDivisionError:
        print("\n (except) errooou, nao pode dividir por zero")
    
    else:
        print(f"\nsua resposta é: {resultado}")

    finally:
        print("\n Estou no finally, isso sempre acontecerá!")

divide(3,2)
divide(3,0)
 