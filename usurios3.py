from flask import Flask, request, render_template_string

app = Flask(__name__)

# Diccionario de usuarios válidos
usuarios = {
    "Cristopher": "Robin2000",
    "Daniella": "Vega1999",
    "Marcelo": "Duoc2025"
}

# HTML del formulario
formulario_html = """
<h2>Ingreso de Usuario (Examen DRY7122)</h2>
<form method="post">
  Nombre de usuario: <input type="text" name="nombre"><br><br>
  Contraseña: <input type="password" name="clave"><br><br>
  <input type="submit" value="Ingresar">
</form>
{% if mensaje %}
<p><strong>{{ mensaje }}</strong></p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def login():
    mensaje = ""
    if request.method == "POST":
        nombre = request.form.get("nombre")
        clave = request.form.get("clave")
        if nombre in usuarios:
            if usuarios[nombre] == clave:
                mensaje = f" Acceso concedido. Bienvenido/a, {nombre}"
            else:
                mensaje = " Contraseña incorrecta."
        else:
            mensaje = " Usuario no válido. Solo se permite Cristopher o Daniella."
    return render_template_string(formulario_html, mensaje=mensaje)

if __name__ == "__main__":
    app.run(port=5800)
