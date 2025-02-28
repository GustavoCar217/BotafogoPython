from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
    path('cursos', views.cursos, name='cursos'),
    path('servicos', views.servicos, name='servicos'),
    path('registrar-usuario', views.registrarUsuario, name='registrar-usuario'),
    path('login', views.login, name='login'),
    path('logout',views.custom_logout, name='deslogar-usuario'),
]
