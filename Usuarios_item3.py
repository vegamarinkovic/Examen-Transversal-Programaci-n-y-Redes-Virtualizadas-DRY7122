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
