from flask import Flask, request
import sqlite3
import hashlib

app = Flask(__name__)

# Crear base de datos si no existe
def crear_bd():
    conn = sqlite3.connect('usuarios.db')
    conn.execute('CREATE TABLE IF NOT EXISTS usuarios (nombre TEXT, password_hash TEXT)')
    conn.close()

# Ruta principal
@app.route('/')
def inicio():
    return "Sistema de gestión de usuarios - Examen DRY7122 (Cristopher y Daniella)"

# Ruta para registrar usuarios (solo Cristopher y Daniella)
@app.route('/agregar/<nombre>/<clave>')
def agregar_usuario(nombre, clave):
    if nombre.lower() not in ['cristopher', 'daniella']:
        return " Solo se permiten registros de los integrantes del grupo: Cristopher y Daniella."

    clave_hash = hashlib.sha256(clave.encode()).hexdigest()
    conn = sqlite3.connect('usuarios.db')
    conn.execute("INSERT INTO usuarios VALUES (?, ?)", (nombre.lower(), clave_hash))
    conn.commit()
    conn.close()
    return f" Usuario {nombre} registrado con clave cifrada."

# Ruta para validar usuarios
@app.route('/validar/<nombre>/<clave>')
def validar_usuario(nombre, clave):
    clave_hash = hashlib.sha256(clave.encode()).hexdigest()
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.execute("SELECT * FROM usuarios WHERE nombre=? AND password_hash=?", (nombre.lower(), clave_hash))
    usuario = cursor.fetchone()
    conn.close()
    
    if usuario:
        return f" Usuario {nombre} validado correctamente."
    else:
        return f" Usuario o clave incorrecta."

if __name__ == '__main__':
    crear_bd()
    app.run(port=5800)

# Ruta para mostrar todos los usuarios registrados
@app.route('/usuarios')
def mostrar_usuarios():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.execute("SELECT nombre FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()

    if not usuarios:
        return "No hay usuarios registrados."

    nombres = [u[0] for u in usuarios]
    lista = "<br>".join(nombres)
    return f"👥 Usuarios registrados:<br>{lista}"


# validar_usuarios.py

# Diccionario de usuarios y contraseñas (puedes cambiar las claves como gustes)
usuarios = {
    "Cristopher": "Robin2000",
    "Daniella": "Vega1999"
}

# Solicitar usuario y contraseña
nombre = input("Ingresa tu nombre de usuario: ")
clave = input("Ingresa tu contraseña: ")

# Verificar si el usuario existe y la contraseña es correcta
if nombre in usuarios:
    if usuarios[nombre] == clave:
        print("✅ Acceso concedido. Bienvenido/a", nombre)
    else:
        print(" Contraseña incorrecta.")
else:
    print(" Usuario no encontrado.")