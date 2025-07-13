from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Base de datos de usuarios (en producción usarías una BD real)
USUARIOS = {
    "Daniella": {"clave": "Vega1999", "nombre": "Daniella Vega"},
    "Cristopher": {"clave": "Robin2000", "nombre": "Cristopher Sepúlveda"},
    "Marcelo": {"clave": "2025", "nombre": "Marcelo Menares"}
}

@app.route("/", methods=["GET", "POST"])
def login():
    mensaje = ""
    if request.method == "POST":
        usuario = request.form.get("usuario")
        clave = request.form.get("clave")
        
        if usuario in USUARIOS and USUARIOS[usuario]["clave"] == clave:
            return redirect(url_for("bienvenida", nombre=USUARIOS[usuario]["nombre"]))
        else:
            mensaje = "❌ Usuario o contraseña incorrectos"
    
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login - Examen DRY7122</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 500px; margin: 0 auto; padding: 20px; }
            form { display: flex; flex-direction: column; gap: 10px; }
            input, button { padding: 10px; font-size: 16px; }
            .error { color: red; }
        </style>
    </head>
    <body>
        <h1>Acceso al sistema</h1>
        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuario" required>
            <input type="password" name="clave" placeholder="Contraseña" required>
            <button type="submit">Ingresar</button>
        </form>
        {% if mensaje %}<p class="error">{{ mensaje }}</p>{% endif %}
    </body>
    </html>
    """
    return render_template_string(html, mensaje=mensaje)

@app.route("/bienvenida/<nombre>")
def bienvenida(nombre):
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Bienvenido</title>
        <style>
            body {{ font-family: Arial; text-align: center; padding: 50px; }}
            h1 {{ color: #2ecc71; }}
        </style>
    </head>
    <body>
        <h1>¡Bienvenido, {nombre}!</h1>
        <p>Sistema de gestión DRY7122</p>
        <p><a href="/">Volver al login</a></p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5800, debug=True)