import sqlite3

conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

conn.execute(
    """
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY,
            nome TEXT,
            email TEXT)
    """
)

conn.commit()
conn.close()