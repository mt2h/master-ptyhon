from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
# render: Devuelve la template que queremos cargar desde la View, pero debe buscarla
#         dentro de mi App (para lo cual debo agregarla en el 'settings.py' en INSTALLED_APPS)

# request: Es un parámetro que permite recibir datos de peticiones a la URL donde se use. 
#          Se debe de pasar a todos los métodos de la vista.

# HttpResponse: Respuesta Http

# redirect: Redirecciona a otras rutas (URL's)

# MTV -> M: Model (BD), T: Vista (HTML, templates), V: Acciones (métodos)
###########################################################################################

layout = '''
    <h1>Sitio web con Django | Victor Robles</h1>
    <hr/>
    <ul>
        <li><a href="/inicio">Inicio</a></li>
        <li><a href="/hola-mundo">Hola Mundo</a></li>
        <li><a href="/pagina-pruebas">Página de pruebas</a></li>
        <li><a href="/contacto">Contacto</a></li>
    </ul>
    <hr/>
'''

def hola_mundo(request):
    #return HttpResponse(layout+'hola_mundo con DJango!!')
    return render(request, 'hola_mundo.html')

def index(request):
    #return HttpResponse("""
    #    <h1>Inicio</h1>
    #    """)

    #html = '''
    #    <h1>Inicio</h1>
    #    <p>Años hasta el 2050:</p>
    #    <ul>
    #'''
    #year=2020
    #while year <=2050:
    #    if year % 2 == 0: #Mostrar sólo los años pares
    #        html += f"<li>{str(year)}</li>"
    #    year += 1
    #html +="</ul>"

    #return HttpResponse(layout+html)

    nombre = 'Victor Robles'
    lenguajes = ['Javascript', 'Python', 'PHP', 'C']
    year = 2020
    rango = range(year, 2051)

    return render(request, 'index.html',  {
        'title': 'Inicio',
        'mi_variable': 'Soy un dato que está en la vista',
        'nombre': nombre,
        'lenguajes': lenguajes,
        'year': year,
        'rango': rango
    })

def pagina(request, redirigir=0):

    #if redirigir == 1:
    #    #return redirect('/inicio/')
    #    #return redirect('/contacto/Victor/Robles')
    #    return redirect('contacto', nombre="Victor", apellido="Robles")

    #return HttpResponse(layout+"""
    #    <h1>Página de mi Web</h1>
    #    """)

    return render(request, 'pagina.html' , {
        'texto': 'Este es mi texto',
        'lista': ["uno", "dos", "tres"]
    }
    )

def contacto(request, nombre="Victor", apellido="Robles"): 
    #Se le pasa los parámetros nombre y apellido a la URL
    #Estos parámetros son opcionales
    #Si se pasan los dos, estos se muestran en la página.
    html = ""
    if nombre and apellido:
        html += "<p>El nombre completo es:</p>"
        html += f" <h3>{nombre} {apellido}</h3>"
    return HttpResponse(layout + html)
