import sqlite3
from flask import *
from banco import get_hash


def usuarios_add_funcao():

    nome = request.form["nome"]
    senha = request.form["senha"]
    tipo = request.form["cargo"]

    senha_hash = get_hash(senha)

    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO usuarios (nome, senha, tipo) VALUES (?, ?, ?)",
        (nome, senha_hash, tipo)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("usuarios"))