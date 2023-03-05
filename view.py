# Importando Sqlite
import sqlite3 as lite

# Criando conexão
con = lite.connect('dados.db')


# Inserindo informações
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario(nome, email, telefone, dia_em, estado, assunto) VALUES(?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)


# Acesar informações
def mostrar_info():
    with con:
        lista = []
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)
        info = cur.fetchall()

        # retornando todas informações do banco
        for i in info:
            lista.append(i)

    return lista


# Atualizar informações
def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET nome=?, email=?, telefone=?, dia_em=?, estado=?, assunto=? WHERE id=?"
        cur.execute(query, i)


# Deletar informações
def deletar_info(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query, i)
