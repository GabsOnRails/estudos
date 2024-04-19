# Módulo para interface gráfica

import tkinter as tk

# 1 -> Criando a janela
janela = tk.Tk()
janela.geometry("300x150")
janela.title("Gerenciador de frases")


# 2 -> Criando o frame
frame = tk.Frame(janela)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# 3 -> Adicionando label
label = tk.Label(frame, text ="olá mundo")
label.pack(fill='x', expand=True)

# 4 -> Input
frase_lab = tk.Label(frame,text="Digite aqui:")
frase_lab.pack (fill='x', expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True)

# 5 -> Função para alterar o texto da label
def click():
    label.config(text=frase_inp.get())

# 6 -> Botão
botao = tk.Button(frame, text="Enviar", command=click)
botao.pack()


janela.mainloop()
