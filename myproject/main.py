from flask import *
from login import *
from recursos import *
from recurso_add import *
from usuarios import *
from usuarios_add import *

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
    if 'token' not in session:
        return redirect(url_for('login'))
    if not usuario_autorizado():
        return "Acesso negado: você não tem permissão para adicionar itens.", 403
    
    return add_recurso_funcao(item_id)

@app.route("/remove/<int:item_id>")
def remove(item_id):
    if 'token' not in session:
        return redirect(url_for('login'))
    if not usuario_autorizado():
        return "Acesso negado: você não tem permissão para remover itens.", 403
    
    return remove_recurso_funcao(item_id)

@app.route("/set/<int:item_id>", methods=["POST"])
def set_quantidade(item_id):
    if 'token' not in session:
        return redirect(url_for('login'))
    if not usuario_autorizado():
        return "Acesso negado: você não tem permissão alterar itens.", 403
    
    return set_quantidade_funcao(item_id)


@app.route("/recursos/add", methods=["GET"])
def add_item_page():
    if not usuario_autorizado():
        return "Acesso negado: você não tem permissão para adicionar itens.", 403

    return render_template("recursos_add.html")

@app.route("/recursos/add", methods=["POST"])
def add_item_post():
    if not usuario_autorizado():
        return "Acesso negado: você não tem permissão para adicionar itens.", 403
    
    return add_novo_recurso_funcao()

@app.route("/delete/<int:item_id>")
def delete(item_id):
    if 'token' not in session:
        return redirect(url_for('login'))
    if not usuario_autorizado():
        return "Acesso negado: você não tem permissão para remover itens.", 403
    
    return delete_funcao(item_id)





@app.route("/usuarios")
def usuarios():
    if 'token' not in session:
        return redirect(url_for('login'))
    
    if not admin_check():
        return "Acesso negado: você não tem permissão para acessar essa pagina.", 403

    return usuarios_funcao()

@app.route("/usuarios/add", methods=["GET"])
def usuarios_add_page():
    if 'token' not in session:
        return redirect(url_for('login'))
    
    if not admin_check():
        return "Acesso negado: você não tem permissão para acessar essa pagina.", 403

    return render_template("usuarios_add.html")

@app.route("/usuarios/add", methods=["POST"])
def usuarios_add_post():
    if not admin_check():
        return "Acesso negado: você não tem permissão para acessar essa pagina.", 403
    
    return usuarios_add_funcao()

@app.route("/usuarios/delete/<int:usuario_id>")
def delete_usuario(usuario_id):
    if 'token' not in session:
        return redirect(url_for('login'))
    if not usuario_autorizado():
        return "Acesso negado: você não tem permissão para remover usuarios.", 403

    
    return delete_usuario_funcao(usuario_id)



@app.route("/about")
def about():

    return '<p>Pagina de about</p>'

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)