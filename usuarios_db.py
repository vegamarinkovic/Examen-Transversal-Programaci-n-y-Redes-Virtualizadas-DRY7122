import sqlite3
import bcrypt

# 1. Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect('usuarios.db')
cursor = conn.cursor()

# 2. Eliminar tabla si existe y crear nueva (esto evita el error)
cursor.execute("DROP TABLE IF EXISTS usuarios")  # ← Borra la tabla antigua
cursor.execute('''
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    nombre TEXT NOT NULL
)
''')

# 3. Definir usuarios con sus contraseñas hasheadas
usuarios = [
    ("Daniella", "Vega1999", "Daniella Vega"),
    ("Cristopher", "Robin2000", "Cristopher Sepúlveda"),
    ("Marcelo", "2025", "Marcelo Menares")
]

# 4. Insertar usuarios con contraseñas hasheadas
for username, password, nombre in usuarios:
    # Generar hash de la contraseña
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    try:
        cursor.execute(
            "INSERT INTO usuarios (username, password_hash, nombre) VALUES (?, ?, ?)",
            (username, password_hash, nombre)
        )
    except sqlite3.IntegrityError:
        print(f"⚠️ El usuario {username} ya existe. Se omitió.")

# 5. Guardar cambios y cerrar conexión
conn.commit()
conn.close()

print("✅ Base de datos 'usuarios.db' creada/actualizada correctamente.")