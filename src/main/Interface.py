import tkinter as tk
from Integracao import respostaIA

class BubblePopup:
    def __init__(self, mestre, texto, duracao):
        self.mestre = mestre
        self.texto = texto
        self.duracao = duracao

        
        x = mestre.winfo_x()
        y = mestre.winfo_y() - 100

        self.popup = tk.Toplevel(mestre)
        self.popup.wm_overrideredirect(True)  
        self.popup.wm_geometry("+{}+{}".format(x, y))
        self.popup.attributes('-topmost', True)  

        self.texto_widget = tk.Text(self.popup, wrap='word', width=42, height=5, font=("Helvetica", 12))
        self.texto_widget.insert('1.0', texto)
        self.texto_widget.pack(side='left', fill='both', expand=True)

        scrollbar = tk.Scrollbar(self.popup, command=self.texto_widget.yview)
        scrollbar.pack(side='right', fill='y')

        self.texto_widget.config(yscrollcommand=scrollbar.set)

        self.popup.attributes("-alpha", 0.0)

        self.fade_in()

        self.popup.after(duracao, self.fade_out)

    def fade_in(self):
        alpha = self.popup.attributes("-alpha")
        if alpha < 1.0:
            alpha += 0.1  
            self.popup.attributes("-alpha", alpha)
            self.popup.after(50, self.fade_in)  

    def fade_out(self):
        alpha = self.popup.attributes("-alpha")
        if alpha > 0.0:
            alpha -= 0.1  
            self.popup.attributes("-alpha", alpha)
            self.popup.after(50, self.fade_out)  
        else:
            self.fechar_popup() 

    def fechar_popup(self):
        self.popup.destroy()

class SobreposicaoTela:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.attributes('-alpha', 0.95)  
        self.raiz.attributes('-topmost', True)  
        self.raiz.overrideredirect(1)  

        self.entrada_usuario = tk.Entry(raiz, font=("Helvetica", 12), width=39)
        self.entrada_usuario.pack(side='left', padx=5)

        self.entrada_usuario.bind('<Return>', lambda evento: self.upload_e_mostrar_popup())

        self.botao_fechar = tk.Button(raiz, text=" X ", command=raiz.destroy)
        self.botao_fechar.pack(side='left', padx=1)

    def upload_e_mostrar_popup(self):
        entrada_usuario = self.entrada_usuario.get()
        self.entrada_usuario.delete(0, 'end')

        resultado = respostaIA(entrada_usuario)
        duracao = (len(resultado.split())) * 256

        instancia_balao_popup = BubblePopup(self.raiz, resultado, duracao)

if __name__ == "__main__":
    raiz = tk.Tk()

    largura = 400
    altura = 50
    x = (raiz.winfo_screenwidth() - largura)
    y = (raiz.winfo_screenheight() - altura) - 50

    raiz.geometry(f'{largura}x{altura}+{x}+{y}')

    sobreposicao = SobreposicaoTela(raiz)
    raiz.mainloop()
