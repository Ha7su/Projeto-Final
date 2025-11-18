import sqlite3
import hashlib



conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

def get_hash(senha):
    enconded_text = senha.encode('utf-8')
    hash_object = hashlib.sha256(enconded_text)
    return hash_object.hexdigest()

def adicionar_usuario():
    nome = input('Digite um nome:')
    senha = input('Digite uma senha:')
    tipo_numero = input('Digite 1 para Administrador \nDigite 2 para Gerente \nDigite 3 para Funcionario: ')
    tipo = 'Administrador' if tipo_numero == '1' else 'Gerente' if tipo_numero == '2' else 'Funcionario' if tipo_numero == '3' else 'Error'

    cursor.execute(
        "INSERT INTO usuarios (nome, senha, tipo) VALUES (?,?,?)",
        (nome, get_hash(senha), tipo)
)
    conexao.commit()

def remover_usuario():
    cursor.execute('SELECT id, nome FROM usuarios')
    for linha in cursor.fetchall():
        print(linha)

    id_remover = int(input('Digite o ID que deseja remover:'))

    cursor.execute('SELECT id FROM usuarios')
    for linha in cursor.fetchall():
        for id in linha:
            if id == id_remover:
                cursor.execute('DELETE FROM usuarios WHERE id = ?', (id_remover,))
                conexao.commit()
                print('Usuario removideo com sucesso!')

def modificar_usuario():
    cursor.execute('SELECT id, nome FROM usuarios')
    for linha in cursor.fetchall():
        print(linha)

    id_update = int(input('Digite o ID que deseja modificar:'))
    
    cursor.execute('SELECT id FROM usuarios')
    for linha in cursor.fetchall():
        for id in linha:
            if id == id_update:
                nome = input('Digite novo nome: ')
                senha = input('Digite nova senha: ')
                tipo_numero = input('Digite 1 para Administrador \nDigite 2 para Gerente \nDigite 3 para Funcionario: ')
                tipo = 'Administrador' if tipo_numero == '1' else 'Gerente' if tipo_numero == '2' else 'Funcionario' if tipo_numero == '3' else 'Error'
                cursor.execute("""UPDATE usuarios
                                  SET nome = ?, senha = ?, tipo = ?
                                  WHERE id = ?;""", (nome, get_hash(senha), tipo, id_update))
                conexao.commit()
                print('Usuario modificado com sucesso!')


def mostrar_usuarios():
    cursor.execute('SELECT * FROM usuarios')
    for linha in cursor.fetchall():
        print(linha)

def adicionar_inventario():
    categoria_numero = input('Digite 1 para Equipamento \nDigite 2 para Veículo \nDigite 3 para Dispositivo de Segurança: ')
    categoria = 'Equipamento' if categoria_numero == '1' else 'Veículo' if categoria_numero == '2' else 'Dispositivo de Segurança' if categoria_numero == '3' else 'Error'
    nome = input('Digite o nome do recurso: ')
    quantidade = input('Digite a quantidade de estoque: ')

    cursor.execute(
        "INSERT INTO inventario (categoria, nome, quantidade) VALUES (?,?,?)",
        (categoria, nome, quantidade)
)
    conexao.commit()


def remover_inventario():
    cursor.execute('SELECT id, nome FROM inventario')
    for linha in cursor.fetchall():
        print(linha)

    id_remover = int(input('Digite o ID que deseja remover:'))

    cursor.execute('SELECT id FROM inventario')
    for linha in cursor.fetchall():
        for id in linha:
            if id == id_remover:
                cursor.execute('DELETE FROM inventario WHERE id = ?', (id_remover,))
                conexao.commit()
                print('Recurso removideo com sucesso!')

def modificar_inventario():
    cursor.execute('SELECT id, nome FROM inventario')
    for linha in cursor.fetchall():
        print(linha)

    id_update = int(input('Digite o ID que deseja modificar:'))
    
    cursor.execute('SELECT id FROM inventario')
    for linha in cursor.fetchall():
        for id in linha:
            if id == id_update:
                categoria_numero = input('Digite 1 para Equipamento \nDigite 2 para Veículo \nDigite 3 para Dispositivo de Segurança: ')
                categoria = 'Equipamento' if categoria_numero == '1' else 'Veículo' if categoria_numero == '2' else 'Dispositivo de Segurança' if categoria_numero == '3' else 'Error'
                nome = input('Digite o nome do recurso: ')
                quantidade = input('Digite a quantidade de estoque: ')
                cursor.execute("""UPDATE inventario
                                  SET categoria = ?, nome = ?, quantidade = ?
                                  WHERE id = ?;""", (categoria, nome, quantidade, id_update))
                conexao.commit()
                print('Recurso modificado com sucesso!')

def mostrar_inventario():
    cursor.execute('SELECT * FROM inventario')
    for linha in cursor.fetchall():
        print(linha)

# Funcao usada para converter todas as senhas em hash:
# def modificar_senha():
#     senhas = cursor.execute('SELECT senha FROM usuarios')
#     hash_senhas = []
#     for i in senhas:
#         hash_senhas.append(get_hash(i[0]))
    
#     print(hash_senhas)
    
#     cursor.executemany(
#     "UPDATE usuarios SET senha = ? WHERE id = ?",
#     [(senha, i+1) for i, senha in enumerate(hash_senhas)]
# )
    
#     conexao.commit()

# modificar_senha()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS usuarios (
#   id INTEGER PRIMARY KEY AUTOINCREMENT,
#   nome TEXT NOT NULL,
#   senha TEXT NOT NULL,
#   tipo TEXT NOT NULL
# );
# """)
# conexao.commit()

# cursor.executemany("""
# INSERT INTO usuarios (nome, senha, tipo)
# VALUES (?, ?, ?)
# """, [
#     ('admin', '123', 'Administrador'),
#     ('Ana Silva', 'senha123', 'Gerente'),
#     ('Bruno Costa', 'abc123', 'Gerente'),
#     ('Carla Nunes', 'carla2025', 'Funcionario'),
#     ('Daniel Rocha', 'dan123', 'Funcionario'),
#     ('Eduardo Lima', 'edu987', 'Gerente'),
#     ('Fernanda Alves', 'f3rna', 'Funcionario'),
#     ('Gustavo Moreira', 'gust@123', 'Funcionario'),
#     ('Helena Dias', 'helena#1', 'Funcionario'),
#     ('Igor Martins', 'igorm', 'Funcionario'),
#     ('Juliana Souza', 'juliana321', 'Gerente'),
#     ('Kleber Santos', 'k!2025', 'Funcionario'),
#     ('Larissa Melo', 'larim', 'Funcionario'),
#     ('Marcos Vinícius', 'marc123', 'Administrador'),
#     ('Natália Gomes', 'natg', 'Funcionario'),
#     ('Otávio Fernandes', 'otavio@2025', 'Gerente'),
#     ('Patrícia Ramos', 'pat123', 'Funcionario'),
#     ('Rafael Oliveira', 'rafa123', 'Funcionario'),
#     ('Simone Pereira', 's1mon3', 'Gerente'),
#     ('Thiago Mendes', 'thiago', 'Funcionario')
# ])
# conexao.commit()

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS inventario (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     categoria TEXT NOT NULL,
#     nome TEXT NOT NULL,
#     quantidade INTEGER NOT NULL
# )
# """)
# conexao.commit()

# cursor.executemany("""
# INSERT INTO inventario (categoria, nome, quantidade)
# VALUES (?, ?, ?)
# """, [
#     ('Equipamento', 'Chave de Fenda', 50),
#     ('Equipamento', 'Martelo', 35),
#     ('Equipamento', 'Alicate', 40),
#     ('Equipamento', 'Furadeira Elétrica', 12),
#     ('Equipamento', 'Serra Circular', 8),
#     ('Equipamento', 'Multímetro Digital', 15),
#     ('Equipamento', 'Lanterna Recarregável', 20),
#     ('Veículo', 'Caminhonete de Serviço', 3),
#     ('Veículo', 'Carro de Patrulha', 4),
#     ('Veículo', 'Moto Utilitária', 6),
#     ('Veículo', 'Van de Transporte', 2),
#     ('Veículo', 'Drone de Inspeção', 5),
#     ('Veículo', 'Caminhão de Carga', 1),
#     ('Dispositivo de Segurança', 'Câmera de Vigilância', 24),
#     ('Dispositivo de Segurança', 'Sensor de Movimento', 18),
#     ('Dispositivo de Segurança', 'Trava Eletrônica', 10),
#     ('Dispositivo de Segurança', 'Alarme Sonoro', 8),
#     ('Dispositivo de Segurança', 'Detector de Fumaça', 30),
#     ('Dispositivo de Segurança', 'Painel de Controle de Segurança', 5),
#     ('Dispositivo de Segurança', 'Sistema de Acesso com Cartão', 12)
# ])
# conexao.commit()