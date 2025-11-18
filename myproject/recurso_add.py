import sqlite3
from flask import *

def usuario_autorizado():
    return "permissao" in session and session["permissao"] in ("Administrador", "Gerente")

def add_novo_recurso_funcao():

    nome = request.form["nome"]
    quantidade = int(request.form["quantidade"])
    categoria = request.form["categoria"]

    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO inventario (categoria, nome, quantidade) VALUES (?, ?, ?)",
        (categoria, nome, quantidade)
    )
    conn.commit()
    conn.close()

    return redirect(url_for("recursos"))