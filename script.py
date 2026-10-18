import sqlite3

conn = sqlite3.connect(":memory:")   # banco temporário, some ao fechar
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE tarefas (
        id INTEGER PRIMARY KEY,
        titulo TEXT,
        concluida INTEGER
    )
""")

# tuplas
titulo = "Estudar SQL"
concluida = 1
cursor.execute("INSERT INTO tarefas (titulo, concluida) VALUES (?, ?)", (titulo, concluida))

titulo = "Estudar Python"
concluida = 1
cursor.execute("INSERT INTO tarefas (titulo, concluida) VALUES (?,?)", (titulo, concluida))

titulo = "Fazer atividade"
concluida = 0
cursor.execute("INSERT INTO tarefas (titulo, concluida) VALUES (?,?)", (titulo, concluida))

conn.commit()   # salva as mudanças

cursor.execute("SELECT id, titulo, concluida FROM tarefas")
linhas = cursor.fetchall()   

# transformando tuplas em um dicionário e coloque numa lista

def linhas_para_dicts(linhas):
    resultado = []
    for linha in linhas:
        d = {"id": linha[0], "titulo": linha[1], "concluida": linha[2]}
        resultado.append(d)
    return resultado

# percorrendo a lista e imprimindo formatado
def mostrar_tarefas(tarefas):
    for tarefa in tarefas:
        if tarefa["concluida"] == 1:
            status = "concluida"
        else:
            status = "pendente"
        print(f"{tarefa['id']} - {tarefa['titulo']} [{status}]")

tarefas = linhas_para_dicts(linhas)
mostrar_tarefas(tarefas)   
       
conn.close()