from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('contato/', views.contato, name = 'contato'),
    path('cursos/', views.cursos, name = 'cursos'),
    path('sobrenos/', views.nos, name = 'sobreNos'),
    path('servicos/', views.servicos, name = 'servicos'),
]