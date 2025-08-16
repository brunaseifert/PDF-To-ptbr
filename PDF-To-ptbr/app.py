import tkinter as tk
from tkinter import filedialog, messagebox
import pdfplumber
from deep_translator import GoogleTranslator
import os

def selecionar_pdf():
    caminho = filedialog.askopenfilename(filetypes=[("Arquivos PDF", "*.pdf")])
    if caminho:
        entrada_pdf.set(caminho)

def salvar_txt(texto):
    caminho_saida = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos TXT", "*.txt")])
    if caminho_saida:
        with open(caminho_saida, 'w', encoding='utf-8') as f:
            f.write(texto)
        messagebox.showinfo("Sucesso", "Texto traduzido salvo com sucesso!")

def traduzir_pdf():
    caminho_pdf = entrada_pdf.get()
    if not caminho_pdf or not os.path.exists(caminho_pdf):
        messagebox.showerror("Erro", "Selecione um arquivo PDF válido.")
        return

    try:
        texto_extraido = ""
        with pdfplumber.open(caminho_pdf) as pdf:
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if texto:
                    texto_extraido += texto + "\n"

        if texto_extraido.strip() == "":
            messagebox.showwarning("Aviso", "Nenhum texto encontrado no PDF.")
            return

        messagebox.showinfo("Aguarde", "Traduzindo o texto, isso pode levar alguns segundos...")

        # Traduzir do inglês para português (Brasil)
        texto_traduzido = GoogleTranslator(source='en', target='pt').translate(texto_extraido)

        salvar_txt(texto_traduzido)

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

# Interface
janela = tk.Tk()
janela.title("PDF para TXT Traduzido (EN → PT-BR)")
janela.geometry("400x200")
janela.resizable(False, False)

entrada_pdf = tk.StringVar()

frame = tk.Frame(janela, padx=20, pady=20)
frame.pack(expand=True, fill="both")

tk.Label(frame, text="Selecione um arquivo PDF em inglês:").pack(anchor="w")

entrada = tk.Entry(frame, textvariable=entrada_pdf, width=40)
entrada.pack(side="left", padx=(0,10))

botao_selecionar = tk.Button(frame, text="Procurar", command=selecionar_pdf)
botao_selecionar.pack(side="left")

botao_converter = tk.Button(janela, text="Traduzir PDF", command=traduzir_pdf, height=2)
botao_converter.pack(pady=20)

janela.mainloop()
