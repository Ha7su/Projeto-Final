from flask import *
from login import *
from recursos import *

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

    return recursos_funcao()

@app.route("/add/<int:item_id>")
def add(item_id):
    return add_recurso_funcao(item_id)

@app.route("/remove/<int:item_id>")
def remove(item_id):
    return remove_recurso_funcao(item_id)

@app.route("/set/<int:item_id>", methods=["POST"])
def set_quantidade(item_id):
    return set_quantidade_funcao(item_id)

@app.route("/delete/<int:item_id>")
def delete(item_id):
    return delete_funcao(item_id)



@app.route("/about")
def about():
    if 'token' not in session:
        return redirect(url_for('login'))

    return '<p>Pagina de about</p>'

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)