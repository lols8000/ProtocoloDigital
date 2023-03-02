# Importando Sqlite
import sqlite3 as lite

#Criando conexão
con = lite.connect('dados.db')

lista = ['Joao Futi Muanda', 'joao@mail.com', 123456789, "12/19/2010", 'Normal', 'gostaria de o consultar pessoalmente']

'''
#Inserindo informações
with con:
    cur = con.cursor()
    query = "INSERT INTO formulario(nome, email, telefone, dia_em, estado, assunto) VALUES(?, ?, ?, ?, ?, ?)"
    cur.execute(query, lista)
'''
#Acesar informações
with con:
    cur = con.cursor()
    query = "SELECT * FROM formulario"
    cur.execute(query)
    info = cur.fetchall()
    print(info)
