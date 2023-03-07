from django.shortcuts import render
from AppCoder.models import Curso, Profesor, Estudiante, Entregable
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudiantesFormulario, EntregableFormulario
# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def cursos(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data

            curso=Curso(nombre=informacion['nombre'], camada=informacion['camada'])
            curso.save()

            return render(request, 'inicio.html')

    else: 
        miFormulario = CursoFormulario()

    return render(request, "cursos.html", {'miFormulario':miFormulario})

def profesores(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data

            profesor=Profesor(nombre=informacion['nombre'], 
                              apellido=informacion['apellido'], 
                              email=informacion['email'], 
                              profesion=informacion['profesion'])
            profesor.save()

            return render(request, 'inicio.html')

    else: 
        miFormulario = ProfesorFormulario()

    return render(request, "Profesores.html", {'miFormulario':miFormulario})

def busquedaCamada(request):
    return render(request, 'inicio.html')

def buscar(request):
    if request.GET['camada']:
        camada = request.GET['camada']
        curso = Curso.objects.filter(camada__icontains=camada)

        return render(request, 'inicio.html', {"cursos":curso, "camada":camada})
    
    else:
        respuesta = 'No enviaste Datos'

    #return HttpResponse(respuesta)
    return render(request, 'inicio.html', {"respuesta":respuesta}) 

def estudiantes(request):
    if request.method == 'POST':
        miFormulario = EstudiantesFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data

            estudiante=Estudiante(nombre=informacion['nombre'],
                                  apellido=informacion['apellido'],
                                  email=informacion['email'])
            estudiante.save()

            return render(request, 'inicio.html')

    else: 
        miFormulario = EstudiantesFormulario()

    return render(request, "estudiantes.html", {'miFormulario':miFormulario})

def entregables(request):
    if request.method == 'POST':
        miFormulario = EntregableFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data

            entregable=Entregable(nombre=informacion['nombre'],
                                  fechaDeEntrega=informacion['fechaDeEntrega'],
                                  entregado=informacion['entregado'])
            entregable.save()

            return render(request, 'inicio.html')

    else: 
        miFormulario = EntregableFormulario()

    return render(request, "entregables.html", {'miFormulario':miFormulario})
            