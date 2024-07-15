import tkinter as tk
from tkinter import messagebox
import random
import string

class CodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Códigos")
        self.root.geometry("400x250")
        
        self.label = tk.Label(root, text="Clique em 'Gerar Código' para criar um novo código:")
        self.label.pack(pady=10)
        
        self.code_display = tk.Entry(root, width=30, font=('Helvetica', 12))
        self.code_display.pack(pady=10)
        
        self.generate_button = tk.Button(root, text="Gerar Código", command=self.generate_code)
        self.generate_button.pack(pady=5)
        
        self.copy_button = tk.Button(root, text="Copiar Código", command=self.copy_code)
        self.copy_button.pack(pady=5)
        
        self.clear_button = tk.Button(root, text="Limpar", command=self.clear_code)
        self.clear_button.pack(pady=5)
        
        self.exit_button = tk.Button(root, text="Sair", command=root.quit)
        self.exit_button.pack(pady=5)
    
    def generate_code(self):
        code = '-'.join([''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for _ in range(4)])
        self.code_display.delete(0, tk.END)
        self.code_display.insert(0, code)
    
    def copy_code(self):
        code = self.code_display.get()
        self.root.clipboard_clear()
        self.root.clipboard_append(code)
        messagebox.showinfo("Copiar Código", "Código copiado para a área de transferência!")
    
    def clear_code(self):
        self.code_display.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = CodeGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
