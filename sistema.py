from tkinter import *


class Sistema(Toplevel):
    
    def __init__(self: object, username: str) -> None:
        super().__init__()
        self.__username = username
        
        largura = 300
        altura = 350
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        x = (largura_tela/2) - (largura/2)
        y = (altura_tela/2) - (altura/2)
        self.geometry('%dx%d+%d+%d' % (largura, altura, x, y))
        self.title("Sistema")
        self.bem_vindo = Label(self, text=f'Bem-vindo ao Sistema, {self.__username}', font=('Arial', 10)).place(relx=0.5, rely=0.1, anchor=CENTER)

if __name__ == 'main.py':
    app = Sistema()
    app.mainloop()
