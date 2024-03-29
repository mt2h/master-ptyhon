from flask import Flask, redirect, url_for, render_template
from datetime import datetime

app = Flask(__name__)

#context processors
@app.context_processor
def date_now():
    return {
        'now': datetime.utcnow()
        }

#endpoints
@app.route('/')
def index():
    edad = 18
    personas = ['Víctor', 'Paco', 'Francisco', 'David']
    #return "Aprendiendo Flask con Víctor Robles"
    return render_template('index.html', 
                           edad=edad,
                           dato1="valor",
                           dato2="valor2",
                           lista=["uno", "dos", "tres"],
                           personas=personas
                        )

@app.route('/informacion')
@app.route('/informacion/<string:nombre>')
@app.route('/informacion/<string:nombre>/<apellidos>')
def informacion(nombre=None, apellidos=None):
    texto = ""
    if nombre != None and apellidos != None:
        #texto = f"<h3>Bienvenido, {nombre} {apellidos}</h3>"
        texto = f"Bienvenido, {nombre} {apellidos}"

    #return f"""
    #    <h1>Página de información</h1>
    #    <p>Esta es la página de información</p>
    #    {texto}
    #"""

    return render_template('informacion.html', 
                           texto=texto
        )

@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion=None):
    if redireccion is not None:
        return redirect(url_for('lenguajes'))

    #return "<h1>Página de contacto</h1>"
    return render_template('contacto.html')

@app.route('/lenguajes-de-programacion')
def lenguajes():
    #return "<h1>Página de lenguajes de programación</h1>"
    return render_template('lenguajes.html')

if __name__ == '__main__':
    app.run(debug=True)