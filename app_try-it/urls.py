from django.urls import path
from recipe import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.login_usuario, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('filtrarreceita/', login_required(views.filtrarreceita), name='filtrarreceita'),
    path('historico/', login_required(views.historico), name='historico'),
    path('novareceita/', login_required(views.novareceita), name='novareceita'),
    path('perfil/', login_required(views.perfil), name='perfil'),
    path('recomendacoes/', login_required(views.recomendacoes), name='recomendacoes'),
    path('atualizacoes/', login_required(views.atualizacoes), name='atualizacoes'),
    path('favoritados/', login_required(views.favoritados), name='favoritados'),
]