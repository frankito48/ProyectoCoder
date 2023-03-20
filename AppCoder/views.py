from django.shortcuts import render
from AppCoder.models import Curso, Profesor, Estudiante, Entregable,Avatar
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudiantesFormulario, EntregableFormulario, UserRegisterForm,AvatarFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppCoder.forms import User, UserRegisterForm, UserEditForm, CursoFormulario, ProfesorFormulario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
# Create your views here.


@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    print(avatares[0].imagen.url)
    return render(request, 'inicio.html', {'url': avatares[0].imagen.url})
     
def login_request(request):


      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

            
                  if user is not None:
                        login(request, user)
                       
                        return render(request,"inicio.html",  {"mensaje":f"Bienvenido {usuario} :)"} )
                  else:
                        
                        return render(request,"inicio.html", {"mensaje":"Error, datos incorrectos"} )

            else:
                        
                        return render(request,"inicio.html" ,  {"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()

      return render(request,"login.html", {'form':form} )

def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"inicio.html" ,  {"mensaje":"Usuario Creado :)"})


      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"registro.html" ,  {"form":form})

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

def leerProfesores(request):
    profesores = Profesor.objects.all()
    contexto = {"profesores":profesores}
    return render(request, "leerProfesores.html", contexto)

def eliminarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()

    profesores = Profesor.objects.all()
    contexto = {"profesores":profesores}
    return render(request, "leerProfesores.html", contexto)

def editarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']

            profesor.save()
            return render(request, "inicio.html")
    else:
        miFormulario = ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido, 'email': profesor.email, 'profesion': profesor.profesion})
    return render(request, "editarprofesor.html", {"miFormulario":miFormulario, "profesor_nombre": profesor_nombre})

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

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data


            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            if informacion['password1'] == informacion['password2']:
                usuario.password = make_password(informacion['password1'])
                usuario.save()
            else:
                return render(request, 'inicio.html', {'mensaje':'Contrasena incorrecta'})


            return render(request, 'inicio.html')
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})


    return render(request, "editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})

@login_required
def agregarAvatar(request):
      if request.method == 'POST':

            miFormulario = AvatarFormulario(request.POST, request.FILES) #aquí mellega toda la información del html

            if miFormulario.is_valid:   #Si pasó la validación de Django


                  u = User.objects.get(username=request.user)
                
                  avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen']) 
      
                  avatar.save()

                  return render(request, "inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= AvatarFormulario() #Formulario vacio para construir el html

      return render(request, "agregarAvatar.html", {"miFormulario":miFormulario})



class CursoList(ListView):
    model = Curso
    template_name = "curso_list.html"

class CursoDetalle(DetailView):
    model = Curso
    template_name = "curso_detalle.html"

class CursoCreacion(CreateView):
    model = Curso
    template_name = "curso_form.html"
    success_url = reverse_lazy("AppCoder:List")
    fields = ['nombre', 'camada']

class CursoUpdate(UpdateView):
    model = Curso
    success_url = "/AppCoder/curso/list"
    template_name = "curso_form.html"
    fields = ['nombre', 'camada']

class CursoDelete(DeleteView):
    model = Curso
    template_name = "curso_confirm_delete.html"
    success_url = "/AppCoder/curso/list"