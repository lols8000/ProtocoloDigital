from tkinter import *
from PIL import Image, ImageTk
from tkinter import Tk, StringVar, ttk
from tkcalendar import Calendar, DateEntry
from datetime import date, datetime

ano_atual = datetime.now().year
date_format = 'dd/MM/yyyy'

################# cores ###############
co0 = "#000000"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  # - profit
co6 = "#038cfc"  # azul
co7 = "#ef5350"  # vermelha
co8 = "#263238"  # + verde
co9 = "#e9edf5"  # sky blue

# Criando Janela
janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

# Definindo estilo e tema da janela
style = ttk.Style(janela)
style.theme_use('clam')

# Criando Frames

# Frame cima
frameCima = Frame(janela, width=1043, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

# Frame meio
frameMeio = Frame(janela, width=1043, height=303, bg=co1, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Frame baixo
frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

# Trabalhando no frame cima

# Carregando imagem cabeçalho
app_img = Image.open('icons8-task.gif')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=' Inventario de Itens', width=900, compound=LEFT, relief=RAISED,
                 anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

# Trabalhando no frame meio

# Criando entradas

# Label Nome
l_nome = Label(frameMeio, text='Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
# Criando input text
e_nome = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_nome.place(x=130, y=11)

# Label Local
l_local = Label(frameMeio, text='Local', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_local.place(x=10, y=40)
# Criando input text
e_local = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_local.place(x=130, y=41)

# Label Descrição
l_descricao = Label(frameMeio, text='Descrição', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_descricao.place(x=10, y=70)
# Criando input text
e_descricao = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_descricao.place(x=130, y=71)

# Label modelo
l_modelo = Label(frameMeio, text='Modelo', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_modelo.place(x=10, y=100)
# Criando input text
e_modelo = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_modelo.place(x=130, y=101)

# Label data da compra
l_cal = Label(frameMeio, text='Data da compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_cal.place(x=10, y=130)
# Criando input calendario
e_cal = DateEntry(frameMeio, date_pattern=date_format, width=12, Background='darkblue', bordewidth=2, year=ano_atual)
e_cal.place(x=130, y=131)

# Label Valor da compra
l_valor = Label(frameMeio, text='Valor da compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_valor.place(x=10, y=160)
# Criando input text
e_valor = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_valor.place(x=130, y=161)

# Label Numero de serie
l_serial = Label(frameMeio, text='Número de série', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_serial.place(x=10, y=190)
# Criando input text
e_serial = Entry(frameMeio, width=30, justify='left', relief=SOLID)
e_serial.place(x=130, y=191)

# Criando botões

# Label Imagem do item
l_carregar = Label(frameMeio, text='Imagem do item', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_carregar.place(x=10, y=220)

# Criando Button Carregar
b_carregar = Button(frameMeio, width=30, text='carregar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE,
                    font=('Ivy 8'), bg=co1, fg=co0)
b_carregar.place(x=130, y=221)

# Carregando imagem botão inserir
app_add = Image.open('icons8-add-new-30.png')
app_add = app_add.resize((20, 20))
app_add = ImageTk.PhotoImage(app_add)

# Criando Button Inserir
b_inserir = Button(frameMeio, image=app_add, width=95, text='  Adicionar'.upper(), compound=LEFT, anchor=NW,
                   overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_inserir.place(x=330, y=10)

# Carregando imagem botão Atualizar
app_att = Image.open('icons8-repeat-50.png')
app_att = app_att.resize((20, 20))
app_att = ImageTk.PhotoImage(app_att)

# Criando Button Atualizar
b_att = Button(frameMeio, image=app_att, width=95, text='  Atualizar'.upper(), compound=LEFT, anchor=NW,
               overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_att.place(x=330, y=45)

# Carregando imagem botão Excluir
app_del = Image.open('icons8-delete-58.png')
app_del = app_del.resize((20, 20))
app_del = ImageTk.PhotoImage(app_del)

# Criando Button Excluir
b_del = Button(frameMeio, image=app_del, width=95, text='  Excluir'.upper(), compound=LEFT, anchor=NW,
               overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_del.place(x=330, y=80)

# Carregando imagem botão Ver item
app_see = Image.open('icons8-eye-30.png')
app_see = app_see.resize((20, 20))
app_see = ImageTk.PhotoImage(app_see)

# Criando Button Ver item
b_see = Button(frameMeio, image=app_see, width=95, text='  Ver item'.upper(), compound=LEFT, anchor=NW,
               overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_see.place(x=330, y=218)

janela.mainloop()
