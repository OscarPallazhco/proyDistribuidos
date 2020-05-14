from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import RegistrarUsuario, ListarUsuario

app_name = 'Usuario'

urlpatterns = [

    path('crear_usuario/', login_required(RegistrarUsuario.as_view()), name='crear_usuario'),
    path('listar_usuario/', login_required(ListarUsuario.as_view()), name='listar_usuario'),

]