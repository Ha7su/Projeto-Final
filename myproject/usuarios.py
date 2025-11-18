from flask import *
import sqlite3


def admin_check():
    return session.get("permissao") in ["Administrador"]

def get_usuarios():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute(""" SELECT id, nome, senha, tipo FROM usuarios """)
    dados = cursor.fetchall()
    conn.close()

    return dados

def usuarios_funcao():
    usuarios = get_usuarios()
    permissao = admin_check()
    return render_template("usuarios.html", usuarios=usuarios, permissao=permissao)

def delete_usuario_funcao(usuario_id):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()

    cursor.execute(" SELECT tipo FROM usuarios WHERE id = ? ",(usuario_id,))
    cargo = cursor.fetchone()
    if cargo[0] == 'Administrador':
        return "Acesso negado: você não tem permissão para deletar administradores.", 403
    
    else:
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (usuario_id,))
        conn.commit()
        conn.close()
        return redirect(url_for("usuarios"))
