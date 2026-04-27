import sqlite3

conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

usuarios = {
    'Mateus': 'mateus@email.com',
    'Eliane': 'eliane@email.com'
    }

for usuario, email in usuarios.items():
    conn.execute(
        """
            INSERT INTO usuarios(nome, email) VALUES (?, ?)
        """,
        (usuario, email)
    )

conn.commit()
conn.close()