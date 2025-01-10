from django.shortcuts import redirect, render
from .models import Servico, Curso
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Lista de serviços
servicosLista = [
    {"nome": "Desenvolvimento Web", "descricao": "Criação de sites e apps", "preco": 2500.00},
    {"nome": "Consultoria", "descricao": "Análise de sistemas", "preco": 1800.00},
    {"nome": "Suporte Técnico", "descricao": "Suporte remoto e presencial", "preco": 500.00},
]

# Lista de cursos
cursosLista = [
    {"nome": "Python Básico", "descricao": "Introdução à programação com Python", "carga_horaria": 40, "preco": 800.00},
    {"nome": "Django Completo", "descricao": "Desenvolvimento web com Django", "carga_horaria": 60, "preco": 1200.00},
    {"nome": "Banco de Dados", "descricao": "Gestão de dados com SQL", "carga_horaria": 50, "preco": 1000.00},
]

# Create your views here.

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def cursos(request):
    return render(request, 'cursos.html')

def servicos(request):
    return render(request, 'servicos.html')

def registrarUsuario(request):
    if request.method == 'POST':
        nome_usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        user = User.objects.create_user(username=nome_usuario, password=senha)
        user.save()
    return render(request, 'home.html') 

def custom_logout(request):
    return render(request,'home.html')

def login(request):
    return render(request, 'login-usuario.html')
