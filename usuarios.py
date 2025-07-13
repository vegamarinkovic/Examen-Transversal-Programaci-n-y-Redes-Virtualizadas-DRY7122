from flask import Flask, request
import sqlite3
import hashlib

app = Flask(__name__)

# Crear base de datos
def crear_bd():
    conn = sqlite3.connect('usuarios.db')
    conn.execute('CREATE TABLE IF NOT EXISTS usuarios (nombre TEXT, password_hash TEXT)')
    conn.close()

@app.route('/')
def inicio():
    return "Sistema de gestión de usuarios"

@app.route('/agregar/<nombre>/<clave>')
def agregar_usuario(nombre, clave):
    clave_hash = hashlib.sha256(clave.encode()).hexdigest()
    conn = sqlite3.connect('usuarios.db')
    conn.execute("INSERT INTO usuarios VALUES (?, ?)", (nombre, clave_hash))
    conn.commit()
    conn.close()
    return f"Usuario {nombre} registrado con clave en hash."

if __name__ == '__main__':
    crear_bd()
    app.run(port=5800)
