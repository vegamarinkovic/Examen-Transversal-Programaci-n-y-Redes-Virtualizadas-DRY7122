import sqlite3
import bcrypt

conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT,
    nombre TEXT
)
''')

usuarios = [
    ("Daniella", "Vega1999", "Daniella Vega"),
    ("Cristopher", "Robin2000", "Cristopher Sepúlveda"),
    ("Marcelo", "2025", "Marcelo Menares")
]

for user, pwd, nombre in usuarios:
    hash_pwd = bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    cursor.execute("INSERT INTO usuarios (username, password_hash, nombre) VALUES (?, ?, ?)",
                  (user, hash_pwd, nombre))

conn.commit()
conn.close()
print("¡Archivo 'usuarios.db' generado con éxito!")