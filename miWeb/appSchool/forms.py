from django import forms

class FormEstudiante(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    mail = forms.EmailField()
    legajo = forms.IntegerField()

class FormProfesor(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    mail = forms.EmailField()
    profesion = forms.CharField(max_length=15)

class FormNota(forms.Form):
    materia = forms.CharField(max_length=15)
    alumno = forms.CharField(max_length=30)
    nota = forms.IntegerField()

class FormMateria(forms.Form):
    nombre = forms.CharField(max_length=15)
    profesor = forms.CharField(max_length=15)