from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle
from django.contrib import messages

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

def crear_articulo(request, title='', content='', public=''):

    articulo = Article(
        title = title,
        content = content,
        public = public
    )

    # # método save() es para guardarlo en la BD.
    articulo.save()

    return HttpResponse(f'<p>Artículo creado: </p><p><strong>Título: </strong>{articulo.title}</p> <p><strong>Contenido: </strong>{articulo.content }</p>')

def save_article(request):
    #if request.method == 'GET':
    if request.method == 'POST':
        #title = request.GET['title']
        #content = request.GET['content']
        #public = request.GET['public']
        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']
        
        if len(title) <= 5:
            return HttpResponse("El título es muy pequeño")

        articulo = Article(
            title = title,
            content = content,
            public = public
        )
        articulo.save()
    
        return HttpResponse(f"Articulo creado: {articulo.title}--->{articulo.content}")

    else:
        return HttpResponse("<h2>No se ha podido crear el artículo</h2>")

    return HttpResponse('')

def create_article(request):
    
    return render(request, 'create_article.html')

def create_full_article(request):
    if request.method == 'POST':
        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            title = data_form.get('title')
            content = data_form['content']
            public = data_form['public']

            articulo = Article(
                title = title,
                content = content,
                public = public
            )

            articulo.save()

            #return HttpResponse(articulo.title + ' ' + articulo.content + ' ' + str(articulo.public))

            #Crear mensaje flash (sesión que solo se muestra una vez)
            messages.success(request, f'Artículo {articulo.title} generado correctamente!')            

            return redirect('articulos')
            
    else:
        formulario = FormArticle()

    return render(
        request, 
        'create_full_article.html',
        {
            'form': formulario
        }
    )

def articulo(request):
    try:
        articulo = Article.objects.get(pk=1)
        #articulo = Article.objects.get(id=1, public=True)
        response = f'Articulo: </br> {articulo.id} - {articulo.title}'
    except:
        response = '<h1>Artículo no encontrado</h1>'
        
    return HttpResponse(response)

def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "Movie created on 2017"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Articulo modificado: {articulo.id}.{articulo.title}")

def articulos(request):
    #articulos = Article.objects.all()
    articulos = Article.objects.all().order_by('-id') #- DESC
    #articulos = Article.objects.all().order_by('-id')[:1]

    #articulos = Article.objects.filter(title="myarticle", id=1)
    #articulos = Article.objects.filter(title__contains="article")
    #articulos = Article.objects.filter(title__exact="myarticle")
    #articulos = Article.objects.filter(title__iexact="myarticle") # no diference between upper and lower text
    #articulos = Article.objects.filter(id__gt=5) # id > 5
    #articulos = Article.objects.filter(id__gte=5) # id >= 5
    #articulos = Article.objects.filter(id__lt=5) # id < 5
    #articulos = Article.objects.filter(id__lte=5, title__contains="articulo") # id <= 5
     
    #articulos = Article.objects.filter(
    #    title="Articulo 1"
    #).exclude(public=False)

    #Para consultas SQL:
    #articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE title = 'Articulo 2' AND public = true")
    
    #articulos = Article.objects.filter(
    #    Q(title__contains="Art") | Q(public__contains=True)
    #)

    return render(request, 'articulos.html', {
        'articulos': articulos
    })

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()

    return redirect('articulos')