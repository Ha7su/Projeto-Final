from flask import *
from login import login_funcao

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    return login_funcao()


@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/recursos")
def recursos():
    return "<p>Pagina de recursos</p>"

@app.route("/funcionarios")
def funcionarios():
    return "<p>Pagina de funcionarios</p>"

if __name__ == '__main__':
    app.run(debug=True)