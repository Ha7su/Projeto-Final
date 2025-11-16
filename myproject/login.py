import sqlite3
import secrets
import hashlib
from banco import get_hash

from flask import *


def validar_login(nome, senha):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND senha = ?", (nome, get_hash(senha)))
    resultado = cursor.fetchone()

    conn.close()
    return resultado

def login_funcao():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']

        if validar_login(nome, senha):
            
            token = secrets.token_hex(16)
            session['token'] = token
            session['usuario'] = nome

            return redirect(url_for('home'))
        else:
            return render_template('login.html', erro="Usuário ou senha incorretos!")

   
    return render_template('login.html')  