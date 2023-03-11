from tkinter import *
from PIL import Image, ImageTk
from tkinter import Tk, StringVar, ttk
from tkcalendar import Calendar, DateEntry
from datetime import date, datetime
from tkinter import messagebox
from view import *
from tkinter import filedialog as fd

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
co8 = "#40E0D0"  # + verde
co9 = "#e9edf5"  # sky blue
co10 = "#00A8FF"  # Azul Royal

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

# criando funções
global tree


# Função inserir
def inserir():
    nome = e_nome.get()
    local = e_local.get()
    descricao = e_descricao.get()
    modelo = e_modelo.get()
    data = e_cal.get()
    valor = e_valor.get()
    serie = e_serial.get()
    imagem = imagem_string

    lista_inserir = [nome, local, descricao, modelo, data, valor, serie, imagem]

    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    inserir_form(lista_inserir)
    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

    e_nome.delete(0, 'end')
    e_local.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_modelo.delete(0, 'end')
    e_cal.delete(0, 'end')
    e_valor.delete(0, 'end')
    e_serial.delete(0, 'end')

    mostrar()


# Função para escolher imagem
def escolher_imagem():
    global imagem, imagem_string, l_imagem
    imagem = fd.askopenfilename()
    imagem_string = imagem

    # Carregando imagem item
    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem)
    l_imagem.place(x=700, y=10)

#Função ver item
def ver_imagem():
    global imagem, imagem_string, l_imagem

    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)

    treev_lista = treev_dicionario['values']

    valor = [int(treev_lista[0])]

    item = ver_item(valor)

    imagem = item[0][8]

    # Carregando imagem ver item
    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMeio, image=imagem)
    l_imagem.place(x=700, y=10)





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

# Criando botões #

# Label Imagem do item
l_carregar = Label(frameMeio, text='Imagem do item', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_carregar.place(x=10, y=220)
# Criando Button Carregar
b_carregar = Button(frameMeio, command=escolher_imagem, width=30, text='carregar'.upper(), compound=CENTER,
                    anchor=CENTER, overrelief=RIDGE,
                    font=('Ivy 8'), bg=co1, fg=co0)
b_carregar.place(x=130, y=221)

# Carregando imagem botão inserir
app_add = Image.open('icons8-add-new-30.png')
app_add = app_add.resize((20, 20))
app_add = ImageTk.PhotoImage(app_add)

# Criando Button Inserir
b_inserir = Button(frameMeio, command=inserir, image=app_add, width=95, text='  Adicionar'.upper(), compound=LEFT,
                   anchor=NW,
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
b_del = Button(frameMeio, image=app_del, width=95, text='  Excluir'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE,
               font=('Ivy 8'), bg=co1, fg=co0)
b_del.place(x=330, y=80)

# Carregando imagem botão Ver item
app_see = Image.open('icons8-eye-30.png')
app_see = app_see.resize((20, 20))
app_see = ImageTk.PhotoImage(app_see)

# Criando Button Ver item
b_see = Button(frameMeio, command=ver_imagem, image=app_see, width=95, text='  Ver item'.upper(), compound=LEFT, anchor=NW,
               overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_see.place(x=330, y=218)

# Label quantidade total de valores
l_total = Label(frameMeio, text='', width=14, height=2, anchor=CENTER, font=('Ivy 17 bold'), bg=co10, fg=co1)
l_total.place(x=450, y=17)
l_total_ = Label(frameMeio, text='  Valor total de todos os itens   ', height=1, anchor=NW, font=('Ivy 10 bold'),
                 bg=co10, fg=co1)
l_total_.place(x=450, y=12)

# Label quantidade total de itens
l_qtd = Label(frameMeio, text='', width=14, height=2, pady=5, anchor=CENTER, font=('Ivy 17 bold'), bg=co10, fg=co1)
l_qtd.place(x=450, y=90)
l_qtd_ = Label(frameMeio, text='  Quantidade total de itens  ', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co10,
               fg=co1)
l_qtd_.place(x=450, y=92)

# Carregando imagem botão Atualizar
app_qr_code = Image.open('qrCode.png')
app_qr_code = app_qr_code.resize((100, 100))
app_qr_code = ImageTk.PhotoImage(app_qr_code)

# Label QR Code itens
app_logo = Label(frameMeio, image=app_qr_code, width=100, relief=RAISED, anchor=NW, bg=co1, fg=co4)
app_logo.place(x=450, y=165)

# Carregando QR code
app_imprimir = Image.open('icons8-send-to-printer-16.png')
app_imprimir = app_imprimir.resize((20, 20))
app_imprimir = ImageTk.PhotoImage(app_imprimir)

# Criando Button imprimir
b_see = Button(frameMeio, image=app_imprimir, width=85, text='  Imprimir'.upper(), compound=LEFT, anchor=NW,
               overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_see.place(x=560, y=165)


# Criando tabela frame baixo
def mostrar():
    global tree

    tabela_head = ['#Item', 'Nome', 'Sala/Área', 'Descrição', 'Marca/Modelo', 'Data da compra', 'Valor da compra',
                   'Número de série']

    lista_itens = ver_form()

    tree = ttk.Treeview(frameBaixo, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)

    hd = ["center", "center", "center", "center", "center", "center", "center", 'center']
    h = [40, 150, 100, 160, 130, 100, 100, 100]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)

    quantidade = [8888, 88]

    for iten in lista_itens:
        quantidade.append(iten[6])

    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)

    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_qtd['text'] = Total_itens


mostrar()
janela.mainloop()
