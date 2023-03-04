from django.urls import path
from appSchool.views import *

urlpatterns = [
path('', inicio, name = 'inicio'),
path('estudiantes/', estudiantes, name = 'estudiantes' ),
path('profesores/', profesores, name='profesores'),
path('materias/', materias , name = 'materias'),
path('notas/', notas, name='notas'),

]




