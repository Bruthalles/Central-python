import tkinter as tk

# Criar a janela principal
root = tk.Tk()
root.title("Minha Janela Tkinter")
root.geometry("300x200")  # Define o tamanho da janela

# Criar um rótulo (label)
label = tk.Label(root, text="Olá, Tkinter!", font=("Arial", 14))
label.pack(pady=10)  # Adiciona o label à janela

# Criar um botão
def clicar():
    label.config(text="Botão clicado!")

botao = tk.Button(root, text="Clique aqui", command=clicar)
botao.pack(pady=5)

# Iniciar o loop da interface gráfica
root.mainloop()
