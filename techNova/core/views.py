from django.shortcuts import redirect, render
from .models import Servico, Curso
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .forms import LoginForm
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


# Registrar novo usuário
def registrarUsuario(request):
    if request.method == 'POST':
        nome_usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        # Verificar se as senhas coincidem
        if senha != confirmar_senha:
            return render(request, 'registrar-usuario.html', {'erro': 'As senhas não coincidem.'})

        # Verificar se o nome de usuário já existe
        if get_user_model().objects.filter(username=nome_usuario).exists():
            return render(request, 'registrar-usuario.html', {'erro': 'Este nome de usuário já está em uso.'})

        # Verificar se o e-mail já está em uso
        if get_user_model().objects.filter(email=email).exists():
            return render(request, 'registrar-usuario.html', {'erro': 'Este e-mail já está em uso.'})

        # Criar o usuário
        user = get_user_model().objects.create_user(username=nome_usuario, email=email, password=senha)
        return redirect('login')  # Redireciona para a página de login após o registro

    return render(request, 'registrar-usuario.html')
def custom_logout(request):
    logout(request)
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
    return render(request, 'login-usuario.html')
