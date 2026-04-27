import sqlite3

conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

cursor.execute(
    """
        SELECT * FROM usuarios
    """
)

dados = cursor.fetchall()

for dado in dados:
    print(dado)