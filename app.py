from flask import Flask, render_template
import os
import mimetypes

# Forzar a Python a registrar el tipo correcto para archivos .js y .css en entornos de producción
mimetypes.add_type('application/javascript', '.js')
mimetypes.add_type('text/css', '.css')

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)