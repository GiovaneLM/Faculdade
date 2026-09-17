import tkinter as tk
from tkinter import messagebox
from datetime import date


janela = tk.Tk()
janela.title("calculo de idade")
janela.geometry("400x300")

ano_atual = date.today().year
print(f'ano atual: {ano_atual}')

def calcular():
    ano_nascimento = int(entry_idade.get())
    resultado = int(ano_atual - ano_nascimento)
    messagebox.showinfo("gg", f"sua idade atual é: {resultado}")

label_idade = tk.Label(janela,text='informe ano em que nasceu: ')
label_idade.grid(row=0,column=0,padx=10,pady=10,sticky="w")
entry_idade = tk.Entry(janela,width=30)
entry_idade.grid(row=0,column=1,padx=10,pady=10)


#botao de cadastro
botao_calcular = tk.Button(janela,text='calcular idade',command=calcular)
botao_calcular.grid(row=2,column=1,pady=10)


janela.mainloop()