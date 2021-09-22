from django.shortcuts import render, HttpResponse, redirect

def root(request):
    return redirect("blogs/")

def index(request):
    return HttpResponse(f"placeholder para luego mostrar lista de blogs")
  
def new(request):
    return HttpResponse(f"placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def create(request):
    return redirect("/")

def show(request,number):
    return HttpResponse(f"placeholder para mostrar el blog numero:{number}")

def edit(request,number):
    return HttpResponse(f"placeholder para editar el blog numero:{number}")   

def destroy(request,number):
    return redirect(f"/")

def json(request):
    return HttpResponse(
        {"Nombre": "Paula"}
    )

def saludar(request, nombre):
    return HttpResponse(f"Hola {nombre}")

def home(request):
    datos = {
        'bandas': ['Gorillaz', 'RHCP', 'Wendy Sulca', 'Radiohead']
    }
    return render(request, 'home.html', datos)


