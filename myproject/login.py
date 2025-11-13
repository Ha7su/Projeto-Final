import sqlite3
from flask import *

# Usuário e senha "fake" só pra exemplo
USER = "admin"
PASSWORD = "123"

def validar_login(usuario, senha):
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios WHERE nome = ? AND senha = ?", (usuario, senha))
    resultado = cursor.fetchone()

    conn.close()
    return resultado  # Retorna None se não encontrar

def login_funcao():
    if request.method == 'POST':
        usuario = request.form['nome']
        senha = request.form['senha']

        if validar_login(usuario, senha):
            return redirect(url_for('home'))
        else:
            return render_template('login.html', erro="Usuário ou senha incorretos!")

    # Se for GET, só mostra o formulário
    return render_template('login.html')  