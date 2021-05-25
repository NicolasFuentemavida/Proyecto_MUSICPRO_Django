from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def productos(request):
    return render(request, 'app/productos.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def donaciones(request):
    return render(request, 'app/donaciones.html')  