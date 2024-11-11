from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cadastro, Receita

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            user = form_usuario.save(commit=False)

            nome = request.POST.get('nome', '')
            sobrenome = request.POST.get('sobrenome', '')
            senha = request.POST.get('senha', '')

            Cadastro.objects.create(
                usuario=user,
                nome=nome,
                sobrenome=sobrenome,
                senha=senha,
            )

            user.save()
            login(request, user)
            return redirect('filtrarreceita')

    else:
        form_usuario = UserCreationForm()

    return render(request, 'app_tryit/pages/cadastro.html', {'form_usuario': form_usuario})

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('filtrarreceita')
        else:
            return render(request, 'app_tryit/pages/login_error.html')

    return render(request, 'registration/login.html')

@login_required
def filtrarreceita(request):
    receitas = Receita.objects.all()
    return render(request, 'app_tryit/pages/filtrarreceita.html', {'receitas': receitas})

def novareceita(request):
    return render(request, 'app_tryit/pages/novareceita.html')

def historico(request):
    return render(request, 'app_tryit/pages/historico.html')

def perfil(request):
    return render(request, 'app_tryit/pages/perfil.html')

def recomendacoes(request):
    return render(request, 'app_tryit/pages/recomendacoes.html')

@login_required
def novareceita(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        ingredientes = request.POST.get('ingredientes')
        Receita.objects.create(nome=nome, ingredientes=ingredientes)

        return redirect('filtrarreceita')

    return render(request, 'app_tryit/pages/novareceita.html')

def atualizacoes(request):
    return render(request, 'app_tryit/pages/atualizacoes.html')

def favoritados(request):
    return render(request, 'app_tryit/pages/favoritados.html')
