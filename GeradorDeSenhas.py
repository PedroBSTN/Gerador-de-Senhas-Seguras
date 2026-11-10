import random
import string
import tkinter as tk
from tkinter import messagebox

# ==========================
# Gerar Senha
# ==========================
def gerar_senha():
    try:
        tamanho = int(entry_tamanho.get())

        if tamanho < 4:
            messagebox.showwarning(
                "Aviso",
                "Use pelo menos 4 caracteres."
            )
            return

        caracteres = ""

        if var_letras.get():
            caracteres += string.ascii_letters

        if var_numeros.get():
            caracteres += string.digits

        if var_especiais.get():
            caracteres += string.punctuation

        if not caracteres:
            messagebox.showwarning(
                "Aviso",
                "Selecione pelo menos uma opção."
            )
            return

        senha = ''.join(
            random.choice(caracteres)
            for _ in range(tamanho)
        )

        resultado_var.set(senha)
        atualizar_forca(senha)

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite um número válido."
        )

# ==========================
# Força da Senha
# ==========================
def atualizar_forca(senha):
    pontos = 0

    if len(senha) >= 8:
        pontos += 1

    if any(c.isupper() for c in senha):
        pontos += 1

    if any(c.islower() for c in senha):
        pontos += 1

    if any(c.isdigit() for c in senha):
        pontos += 1

    if any(c in string.punctuation for c in senha):
        pontos += 1

    if pontos <= 2:
        lbl_forca.config(
            text="🔴 Fraca",
            fg="red"
        )
    elif pontos <= 4:
        lbl_forca.config(
            text="🟡 Média",
            fg="orange"
        )
    else:
        lbl_forca.config(
            text="🟢 Forte",
            fg="green"
        )

# ==========================
# Copiar Senha
# ==========================
def copiar_senha():
    senha = resultado_var.get()

    if senha:
        janela.clipboard_clear()
        janela.clipboard_append(senha)

        messagebox.showinfo(
            "Copiado",
            "Senha copiada!"
        )

# ==========================
# Interface
# ==========================
janela = tk.Tk()
janela.title("Gerador de Senhas Seguras")
janela.geometry("450x350")
janela.resizable(False, False)

titulo = tk.Label(
    janela,
    text="🔐 Gerador de Senhas",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=10)

tk.Label(
    janela,
    text="Tamanho da senha:"
).pack()

entry_tamanho = tk.Entry(janela)
entry_tamanho.insert(0, "12")
entry_tamanho.pack(pady=5)

var_letras = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_especiais = tk.BooleanVar(value=True)

tk.Checkbutton(
    janela,
    text="Letras",
    variable=var_letras
).pack()

tk.Checkbutton(
    janela,
    text="Números",
    variable=var_numeros
).pack()

tk.Checkbutton(
    janela,
    text="Caracteres especiais",
    variable=var_especiais
).pack()

tk.Button(
    janela,
    text="Gerar Senha",
    command=gerar_senha,
    bg="#2196F3",
    fg="white"
).pack(pady=10)

resultado_var = tk.StringVar()

tk.Entry(
    janela,
    textvariable=resultado_var,
    font=("Arial", 12),
    justify="center",
    width=30
).pack(pady=5)

tk.Button(
    janela,
    text="Copiar",
    command=copiar_senha,
    bg="#4CAF50",
    fg="white"
).pack()

lbl_forca = tk.Label(
    janela,
    text="Força da senha",
    font=("Arial", 12, "bold")
)
lbl_forca.pack(pady=15)

janela.mainloop()
