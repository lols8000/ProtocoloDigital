from tkinter import *
from cadastroUsuarios import cadastrarUsuario


def menuInicial():
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
    app_nome = Label(frame_top, text='Menu Inicial', anchor=NW, font=('Ivy 16 bold'), bg=co2, fg=co1,
                     relief='flat')
    app_nome.place(x=90, y=15)

    def botaoCadastrarUsuario():
        janela.destroy()
        cadastrarUsuario()

    def botaoCadastrarItem():
        # janela.destroy()
        # cadastrarItem()
        print("Em construção")

    def botaoSair():
        janela.destroy()

    # Botão Cadastrar usuário
    b_login = Button(frame_baixo, command=botaoCadastrarUsuario, text='Cadastrar usuários', width='37', height='5',
                     font=('Ivy 9 bold'), bg=co6, fg=co1,
                     relief='raised', overrelief='ridge')
    b_login.place(x=20, y=30)

    # Botão Cadastrar itens
    b_login = Button(frame_baixo, command='', text='Cadastrar Itens', width='37', height='5', font=('Ivy 9 bold'),
                     bg=co6, fg=co1,
                     relief='raised', overrelief='ridge')
    b_login.place(x=20, y=120)

    # Botão Sair
    b_login = Button(frame_baixo, command=botaoSair, text='Sair', width='37', height='5', font=('Ivy 9 bold'), bg=co7,
                     fg=co1,
                     relief='raised', overrelief='ridge')
    b_login.place(x=20, y=220)

    janela.mainloop()

menuInicial()
