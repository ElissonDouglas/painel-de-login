from tkinter import *
from tkinter import messagebox
from csv import DictReader, writer
from utils import Authentication, pass_gen
from sistema import Sistema

usuarios = []

with open('usuarios.csv', 'r') as arquivo:
    leitor = DictReader(arquivo)
    next(leitor)
    for linha in leitor:
        usuarios.append(linha)


def logar(user, password) -> None:
    janela.user.set('')
    janela.password.set('')
    auth = Authentication(user, password)
    if auth.login_authentication():
        sys = Sistema(user)
    else:
        messagebox.showerror('Erro', 'Usuário ou senha incorretos')


def abrir_tela_registro() -> None:
    def gerar_senha() -> None:
        senha = pass_gen()
        return senha
    
    def registrar(user, password) -> None:
        checar = Authentication(user, password)
        if checar.validate() and checar.exist() == False:
            with open('usuarios.csv', 'a') as arquivo:
                escritor = writer(arquivo)
                escritor.writerow([user, password])
                texto = f"Usuário '{user}' registrado com sucesso"
                messagebox.showinfo('Sucesso', texto)
                registro.destroy()
        elif checar.exist() == True:
            label1 = Label(registro, text='Este usuário já existe.', fg='red', background='white')
            label1.place(relx=0.5, rely=0.6, anchor=CENTER)
            label1.after(1000, label1.destroy)
        elif not checar.validate():
            label1 = Label(registro, text='Sua senha deve conter no mínimo:\n* Oito caracteres,\n*Letras maiúsculas e minúsculas\n*Números.', fg='red', background='white')
            label1.place(relx=0.5, rely=0.67, anchor=CENTER)
            label1.after(3000, label1.destroy)
        

    registro= Toplevel(janela)
    registro.config(bg='white')
    registro.title('Registro')
    largura=300
    altura=350
    largura_tela=registro.winfo_screenwidth()
    altura_tela=registro.winfo_screenheight()
    x=(largura_tela/2) - (largura/2)
    y=(altura_tela/2) - (altura/2)
    registro.geometry('%dx%d+%d+%d' % (largura, altura, x, y))
    Label(registro, text='Registrar', font=('Arial', 20),
          background='white').place(relx=0.5, rely=0.1, anchor=CENTER)
    Label(registro, text='Usuário:', background='white').place(
        relx=0.18, rely=0.2, anchor=CENTER)
    Label(registro, text='Senha:', background='white').place(
        relx=0.18, rely=0.3, anchor=CENTER)
    user_registro=StringVar()
    pass_registro=StringVar()
    entrada=Entry(registro, width=15, textvariable=user_registro).place(
    relx=0.5, rely=0.2, anchor=CENTER)
    entrada2=Entry(registro, width=15, textvariable=pass_registro, show='*').place(
    relx=0.5, rely=0.3, anchor=CENTER)
    botao=Button(registro, text='Registrar', command=lambda: [registrar(
    user_registro.get(), pass_registro.get()), user_registro.set(''), pass_registro.set('')]).place(relx=0.5, rely=0.39, anchor=CENTER)
    # Botão gerar senha
    gen_senha=StringVar()
    generated=Label(registro, textvariable=gen_senha, fg='green',background='white', font=('Arial', 10))
    generated.place(relx=0.5, rely=0.85, anchor=CENTER)
    Button(registro, text='Gerar e copiar senha', command=lambda: [generated.clipboard_clear(), gen_senha.set(gerar_senha()), generated.clipboard_append(gen_senha.get())]).place(relx=0.5, rely=0.93, anchor=CENTER)


# [generated.clipboard_clear(), gen_senha.set(pass_gen()), generated.clipboard_append(gen_senha.get()), generated.after(5000, generated.destroy())]



janela=Tk()
largura=500
altura=500
largura_tela=janela.winfo_screenwidth()
altura_tela=janela.winfo_screenheight()
x=(largura_tela/2) - (largura/2)
y=(altura_tela/2) - (altura/2)
janela.geometry('%dx%d+%d+%d' % (largura, altura, x, y))  # Tamanho da tela
"""Abrir o app no meio da tela"""

janela.title("Painel de Login")  # Título do app
janela.resizable(False, False)  # Não-redimensionável
janela.configure(background='#5b6370')
img=PhotoImage(file='logo(1).png')
frame1=LabelFrame(janela, width=300, height=350, background='white')
frame1.place(relx=0.5, rely=0.5, anchor=CENTER)
Label(frame1, image=img, background='white').place(
    relx=0.5, rely=0.2, anchor=CENTER)
Label(frame1, text='Usuário:', background='white').place(
    relx=0.18, rely=0.4, anchor=CENTER)
Label(frame1, text='Senha:', background='white').place(
    relx=0.18, rely=0.5, anchor=CENTER)

label1=Label(frame1, text="Não tem uma conta?", bg='white',
               fg='black').place(relx=0.5, rely=0.8, anchor=CENTER)
registre=Button(frame1, text="Registre-se", bg='white', fg='black',
                  command=lambda: abrir_tela_registro()).place(relx=0.5, rely=0.9, anchor=CENTER)

# Entradas (username e password)
janela.user=StringVar()
janela.password=StringVar()
entrada_user=Entry(frame1, width=15, textvariable=janela.user).place(
    relx=0.5, rely=0.4, anchor=CENTER)
entrada_pass=Entry(janela, width=15, textvariable=janela.password,
                     show='*').place(relx=0.5, rely=0.5, anchor=CENTER)

# Botão Entrar
login=Button(janela, text='Entrar', background='#33ccca', activebackground='#5fe8e6', command=lambda: logar(
    janela.user.get(), janela.password.get())).place(relx=0.5, rely=0.6, anchor=CENTER)


if __name__ == "__main__":
    janela.mainloop()
