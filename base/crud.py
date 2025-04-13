import sqlite3

# Função para conectar ao banco de dados
def conectar():
    return sqlite3.connect("tarefas.db")


import sqlite3

# Função para conectar ao banco de dados
def conectar():
    return sqlite3.connect("tarefas.db")

# Função para adicionar uma tarefa
def adicionar_tarefa(descricao, data, status="pendente"):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    INSERT INTO tarefas (descricao, data, status)
    VALUES (?, ?, ?)
    """, (descricao, data, status))
    conexao.commit()
    conexao.close()

# Função para listar todas as tarefas
def listar_tarefas():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conexao.close()
    return tarefas

# Função para atualizar o status de uma tarefa
def atualizar_status(id, novo_status):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    UPDATE tarefas
    SET status = ?
    WHERE id = ?
    """, (novo_status, id))
    conexao.commit()
    conexao.close()

# Função para deletar uma tarefa
def deletar_tarefa(id):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()

    






















