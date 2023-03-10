from django.shortcuts import render
from appSchool.forms import *
from appSchool.models import *
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request , 'appSchool/inicio.html')

def estudiantes(request):
    if request.method == 'POST':
        formulario = FormEstudiante(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data

            estudiante = Estudiante(nombre = info['nombre'].title() , apellido = info['apellido'].title() , mail = info['mail'] , legajo = info['legajo'])
            estudiante.save()

            return render(request, 'appSchool/inicio.html')

    else:
        formulario = FormEstudiante()

    return render(request , 'appSchool/estudiantes.html' , {'formulario':formulario})

def profesores(request):
    if request.method == 'POST':
        formulario = FormProfesor(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data

            profesor = Profesor(nombre = info['nombre'].title() , apellido = info['apellido'].title() , mail = info['mail'] , profesion = info['profesion'])
            profesor.save()

            return render(request, 'appSchool/inicio.html')

    else:
        formulario = FormProfesor()

    return render(request , 'appSchool/profesores.html' , {'formulario':formulario})


def materias(request):
    if request.method == 'POST':
        formulario = FormMateria(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data

            materia = Materia(nombre = info['nombre'].title() , profesor = info['profesor'].title())
            materia.save()

            return render(request, 'appSchool/inicio.html')

    else:
        formulario = FormMateria()

    return render(request , 'appSchool/materias.html' , {'formulario':formulario})

def notas(request):
    
    if request.method == 'POST':
        
        formulario = FormNota(request.POST)

        if formulario.is_valid():
            info = formulario.cleaned_data

            nota = Nota(materia = info['materia'].title() , alumno = info['alumno'].title() , nota = info['nota'])
            nota.save()

            return render(request, 'appSchool/inicio.html')

    else:
        formulario = FormNota()

    return render(request , 'appSchool/notas.html' , {'formulario':formulario})


def contacto(request):
    return render(request , 'appSchool/contacto.html' )


def buscarNotas(request):
    
    if request.GET['alumno']:
        alumno = request.GET['alumno']
        objeto = Nota.objects.filter(alumno__icontains = alumno)
       
        if len(objeto) == 0:
             return render(request , 'appSchool/buscarNotas.html', {'vacio':1})

        return render(request , 'appSchool/buscarNotas.html', {'objeto':objeto , 'alumno':alumno})
    
    else:
        return HttpResponse('No se ingresaron datos')
    
def buscarEstudiante(request):
  
    if request.GET['legajo']:
        legajo = request.GET['legajo']
        objeto = Estudiante.objects.filter(legajo__icontains = legajo)

        if len(objeto) == 0:
              return render(request , 'appSchool/buscarEstudiantes.html', {'vacio':1})

        return render(request , 'appSchool/buscarEstudiantes.html', {'objeto':objeto , 'legajo':legajo})
    
    else:
        return HttpResponse('No se ingresaron datos')
    

def buscarMaterias(request):
   
    if request.GET['nombre']:

        nombre = request.GET['nombre']
        objeto = Materia.objects.filter(nombre__icontains = nombre)

        if len(objeto) == 0:
              return render(request , 'appSchool/buscarMaterias.html', {'vacio':1})

        return render(request , 'appSchool/buscarMaterias.html', {'objeto':objeto , 'nombre':nombre})
    
    else:
        return HttpResponse('No se ingresaron datos')
       
def buscarProfesores(request):

    if request.GET['nombre']:

        nombre = request.GET['nombre']
        objeto = Profesor.objects.filter(nombre__icontains = nombre)

        if len(objeto) == 0:
              return render(request , 'appSchool/buscarProfesores.html', {'vacio':1})

        return render(request , 'appSchool/buscarProfesores.html', {'objeto':objeto , 'nombre':nombre})
    
    else:
        return HttpResponse('No se ingresaron datos')
