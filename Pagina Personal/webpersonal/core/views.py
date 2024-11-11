from django.shortcuts import render, HttpResponse

# html_base = """ 
#     <html>
#         </head>
#             <h1>Web Personal</h1>
#             <ul>
#                 <li><a href="/">Principal</a></li>
#                 <li><a href="/about-me/">Sobre Mi</a></li>
#                 <li><a href="/portfolio/">Portafolio de Evidencia</a></li>
#                 <li><a href="/contact/">Contacto</a></li>
#             </ul>
#         </head>
# """

# Create your views here.
def home(request):
    # return HttpResponse(html_base + "<h1>Principal</h1>")
    return render(request, "core/home.html")  # Equivalente a la línea anterior

def about(request):
    # return HttpResponse(html_base + "<h1>Acerca de mi...</h1><p>Hola soy Gonzalo y soy programador</p>")
    return render(request, "core/aboutme.html") # Equivalente a la línea anterior

def portfolio(request):
    # return HttpResponse(html_base + "<h1>Portafolio</h1><p>Aquí irán mis proyectos</p>")
    return render(request, "core/portfolio.html") # Equivalente a la línea anterior

def contact(request):
    # return HttpResponse(html_base + "<h1>Contacto</h1><p>Si deseas contactarme, escríbeme aquí</p>")
    return render(request, "core/contact.html") # Equivalente a la línea anterior