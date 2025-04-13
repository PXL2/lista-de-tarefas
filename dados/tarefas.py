import sqlite3

conexao = sqlite3.connect("tarefas.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    data TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('pendente', 'concluido'))
)
""")

conexao.commit()
conexao.close()
