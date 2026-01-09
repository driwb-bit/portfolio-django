from django.shortcuts import render
from .models import Proyecto

def home(request):
    # Traemos todos los proyectos de la base de datos
    proyectos = Proyecto.objects.all()
    
    # Renderizamos el HTML enviándole los datos
    return render(request, 'portfolio/index.html', {'proyectos': proyectos})