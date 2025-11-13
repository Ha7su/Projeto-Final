from flask import *
from login import *

app = Flask(__name__)
app.secret_key = "90d4f7b25a6c997c"

@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    return login_funcao()

@app.route("/home")
def home():
    if 'token' not in session:
        return redirect(url_for('login'))

    return render_template("home.html", usuario=session['usuario'])

@app.route("/recursos")
def recursos():
    if 'token' not in session:
        return redirect(url_for('login'))

    return '<p>Pagina de recursos</p>'

@app.route("/funcionarios")
def funcionarios():
    if 'token' not in session:
        return redirect(url_for('login'))

    return '<p>Pagina de funcionaros</p>'

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)