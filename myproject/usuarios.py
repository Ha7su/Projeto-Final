from flask import *
import sqlite3


def admin_check():
    return session.get("permissao") in ["Administrador"]

def get_usuarios():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    # cursor.execute("SELECT id, categoria, nome, quantidade FROM inventario")
    cursor.execute(""" SELECT id, nome, senha, tipo FROM usuarios """)
    dados = cursor.fetchall()
    conn.close()

    return dados


def usuarios_funcao():
    usuarios = get_usuarios()
    permissao = admin_check()
    return render_template("usuarios.html", usuarios=usuarios, permissao=permissao)