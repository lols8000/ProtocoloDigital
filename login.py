from tkinter import *
from view import *
from tkinter import messagebox
from janelaInicial import menuInicial


def logar():
    ################# cores ###############
    co0 = "#f0f3f5"  # Preta
    co1 = "#feffff"  # branca
    co2 = "#4fa882"  # verde
    co3 = "#38576b"  # valor
    co4 = "#403d3d"  # letra
    co5 = "#e06636"  # - profit
    co6 = "#038cfc"  # azul
    co7 = "#ef5350"  # vermelha
    co8 = "#263238"  # + verde
    co9 = "#e9edf5"  # sky blue

    ################# criando janela ###############

    janela = Tk()
    janela.title("")
    janela.geometry('310x403')
    janela.configure(background=co9)
    janela.resizable(width=False, height=False)

    frame_top = Frame(janela, width=310, height=50, bg=co2, relief='flat')
    frame_top.grid(row=0, column=0)

    frame_baixo = Frame(janela, width=310, height=403, bg=co9, relief='flat')
    frame_baixo.grid(row=1, column=0)

    ################# Label top ###############
    app_nome = Label(frame_top, text='Protocolo Digital', anchor=NW, font=('Ivy 16 bold'), bg=co2, fg=co1,
                     relief='flat')
    app_nome.place(x=70, y=15)

    def login():
        username = e_usuario.get()
        password = e_senha.get()

        if verify_user(username, password):
            janela.destroy()
            menuInicial()
        else:
            messagebox.showerror('Erro', 'Usuário ou senha não conferem')
            e_usuario.delete(0, 'end')
            e_senha.delete(0, 'end')

    ################# Configurando frame baixo ###############

    # Usuario
    l_usuario = Label(frame_baixo, text='Usuário *', anchor=NW, font=('Ivy 10 bold'), bg=co9, fg=co4, relief='flat')
    l_usuario.place(x=10, y=20)
    e_usuario = Entry(frame_baixo, width=45, justify='left', relief='solid')
    e_usuario.place(x=15, y=50)

    # Senha
    l_senha = Label(frame_baixo, text='Senha *', anchor=NW, font=('Ivy 10 bold'), bg=co9, fg=co4, relief='flat')
    l_senha.place(x=10, y=80)
    e_senha = Entry(frame_baixo, width=45, justify='left', relief='solid', show='*')
    e_senha.place(x=15, y=110)

    # Botão Login
    b_login = Button(frame_baixo, command=login, text='Entrar', width='37', font=('Ivy 9 bold'), bg=co6, fg=co1,
                     relief='raised', overrelief='ridge')
    b_login.place(x=15, y=250)

    janela.mainloop()

#logar()