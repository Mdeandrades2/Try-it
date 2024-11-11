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

            # Verifique se 'nome' está presente na solicitação antes de acessá-lo
            nome = request.POST.get('nome', '')
            sobrenome = request.POST.get('sobrenome', '')
            senha = request.POST.get('senha', '')

            # Agora, criamos uma instância do modelo Cadastro e associamos ao usuário
            Cadastro.objects.create(
                usuario=user,
                nome=nome,
                sobrenome=sobrenome,
                senha=senha,
                # Adicione outras informações conforme necessário
            )

            user.save()
            login(request, user)
            return redirect('filtrarreceita')  # Redirecionar para a página de filtrar receitas

    else:
        form_usuario = UserCreationForm()

    return render(request, 'recipe/pages/cadastro.html', {'form_usuario': form_usuario})




def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Verifique se o usuário está cadastrado
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('filtrarreceita')  # Redirecione para a página de filtrar receitas
        else:
            # Usuário não cadastrado, retorne alguma página de erro ou mensagem
            return render(request, 'recipe/pages/login_error.html')

    return render(request, 'registration/login.html')

@login_required
def filtrarreceita(request):
    receitas = Receita.objects.all()
    return render(request, 'recipe/pages/filtrarreceita.html', {'receitas': receitas})

def novareceita(request):
    return render(request, 'recipe/pages/novareceita.html')

def historico(request):
    return render(request, 'recipe/pages/historico.html')

def perfil(request):
    return render(request, 'recipe/pages/perfil.html')

def recomendacoes(request):
    return render(request, 'recipe/pages/recomendacoes.html')

@login_required
def novareceita(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        ingredientes = request.POST.get('ingredientes')
        Receita.objects.create(nome=nome, ingredientes=ingredientes)

        return redirect('filtrarreceita')

    return render(request, 'recipe/pages/novareceita.html')

def atualizacoes(request):
    return render(request, 'recipe/pages/atualizacoes.html')

def favoritados(request):
    return render(request, 'recipe/pages/favoritados.html')
