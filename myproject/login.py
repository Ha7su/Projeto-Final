from flask import *

# Usuário e senha "fake" só pra exemplo
USER = "admin123"
PASSWORD = "1234"

def login_funcao():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']

        if usuario == USER and senha == PASSWORD:
            # Redireciona para a página inicial após login bem-sucedido
            return redirect(url_for('home'))
        else:
            # Retorna a página de login com mensagem de erro
            return render_template('login.html', erro="Usuário ou senha incorretos!")

    # Se for GET, só mostra o formulário
    return render_template('login.html')  

if __name__ == '__main__':
    app.run(debug=True)