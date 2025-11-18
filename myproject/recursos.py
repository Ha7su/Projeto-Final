from flask import *
import sqlite3
from login import permissao_check


def get_inventario():
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    # cursor.execute("SELECT id, categoria, nome, quantidade FROM inventario")
    cursor.execute("""
        SELECT * FROM inventario
        ORDER BY 
            CASE categoria
                WHEN 'Equipamento' THEN 1
                WHEN 'Veículo' THEN 2
                WHEN 'Dispositivo de Segurança' THEN 3
                ELSE 4
            END,
            nome ASC
    """)
    dados = cursor.fetchall()
    conn.close()


    return dados

def recursos_funcao():
    inventario = get_inventario()
    permissao = permissao_check()
    return render_template("recursos.html", inventario=inventario, permissao=permissao)

def update_quantidade(item_id, nova_qtd):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE inventario SET quantidade = ? WHERE id = ?", (nova_qtd, item_id))
    conn.commit()
    conn.close()

def add_recurso_funcao(item_id):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE inventario SET quantidade = quantidade + 1 WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("recursos"))

def remove_recurso_funcao(item_id):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE inventario SET quantidade = quantidade - 1 WHERE id = ? AND quantidade > 0", (item_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("recursos"))

def set_quantidade_funcao(item_id):
    nova_qtd = int(request.form["quantidade"])
    update_quantidade(item_id, nova_qtd)
    return redirect(url_for("recursos"))

def delete_funcao(item_id):
    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM inventario WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("recursos"))