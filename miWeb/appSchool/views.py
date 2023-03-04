from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request , 'appSchool/inicio.html')

def estudiantes(request):
    return render(request , 'appSchool/estudiantes.html')

def profesores(request):
    return render(request , 'appSchool/profesores.html')

def materias(request):
    return render(request , 'appSchool/materias.html')

def notas(request):
    return render(request , 'appSchool/notas.html')