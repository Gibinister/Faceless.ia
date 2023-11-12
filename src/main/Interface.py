import tkinter as tk
from Integracao import respostaIA

class BubblePopup:
    def __init__(self, mestre, texto, duracao=3000):
        self.mestre = mestre
        self.texto = texto
        self.duracao = duracao

        # Ajusta as coordenadas para posicionar o popup acima da sobreposição
        x = mestre.winfo_x() + 50
        y = mestre.winfo_y() - 100

        self.popup = tk.Toplevel(mestre)
        self.popup.wm_overrideredirect(True)  # Remove as decorações da janela
        self.popup.wm_geometry("+{}+{}".format(x, y))
        self.popup.attributes('-topmost', True)  # Define o popup como o mais alto

        self.texto_widget = tk.Text(self.popup, wrap='word', width=30, height=5, font=("Helvetica", 12))
        self.texto_widget.insert('1.0', texto)
        self.texto_widget.pack(side='left', fill='both', expand=True)

        scrollbar = tk.Scrollbar(self.popup, command=self.texto_widget.yview)
        scrollbar.pack(side='right', fill='y')

        self.texto_widget.config(yscrollcommand=scrollbar.set)

        self.popup.after(duracao, self.fechar_popup)

    def fechar_popup(self):
        self.popup.destroy()

class SobreposicaoTela:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.attributes('-alpha', 0.95)  # Define o nível de transparência
        self.raiz.attributes('-topmost', True)  # Mantém a janela no topo
        self.raiz.overrideredirect(1)  # Remove as decorações da janela

        # Cria uma caixa de entrada para a entrada do usuário
        self.entrada_usuario = tk.Entry(raiz, font=("Helvetica", 12), width=39)
        self.entrada_usuario.pack(side='left', padx=5)

        # Vincula o evento <Return> à função upload_and_show_popup
        self.entrada_usuario.bind('<Return>', lambda evento: self.upload_e_mostrar_popup())

        # Cria um botão para fechar a janela
        self.botao_fechar = tk.Button(raiz, text=" X ", command=raiz.destroy)
        self.botao_fechar.pack(side='left', padx=1)

    def upload_e_mostrar_popup(self):
        entrada_usuario = self.entrada_usuario.get()
        self.entrada_usuario.delete(0, 'end')

        # Chama a função Python de outro arquivo (Integracao.py), READICIONAR COM INTEGRAÇÃO FEIA
        # resultado = respostaIA(entrada_usuario)
        # duracao = (len(resultado.split())) * 256

        # Mostra o resultado no popup de balão
        instancia_balao_popup = BubblePopup(self.raiz, "resultado", duracao=10000)

if __name__ == "__main__":
    raiz = tk.Tk()

    # Define o tamanho e a posição da janela
    largura = 400
    altura = 50
    x = (raiz.winfo_screenwidth() - largura)
    y = (raiz.winfo_screenheight() - altura) - 50

    raiz.geometry(f'{largura}x{altura}+{x}+{y}')

    sobreposicao = SobreposicaoTela(raiz)
    raiz.mainloop()
