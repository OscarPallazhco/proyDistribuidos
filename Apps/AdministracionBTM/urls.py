from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

app_name = 'AdministracionBTM'

urlpatterns = [
    path('crear_cliente/', login_required(CrearCliente.as_view()), name='crear_cliente'),
    path('listar_cliente/', login_required(ListadoCliente.as_view()), name='listar_cliente'),
    path('editar_cliente/<str:pk>', login_required(ActualizarCliente.as_view()), name='editar_cliente'),
    path('eliminar_cliente/<str:pk>', login_required(EliminarCliente.as_view()), name='eliminar_cliente'),

    path('listar_cotizacion/', login_required(ListadoCotizacion.as_view()), name='listar_cotizacion'),
    path('crear_cotizacion/', login_required(CrearCotizacion.as_view()), name='crear_cotizacion'),
    path('editar_cotizacion/<int:pk>', login_required(ActualizarCotizacion.as_view()), name='editar_cotizacion'),
    path('eliminar_cotizacion/<int:pk>', login_required(EliminarCotizacion.as_view()), name='eliminar_cotizacion'),

    path('listar_item/', login_required(ListadoItem.as_view()), name='listar_item'),
    path('crear_item/', login_required(CrearItem.as_view()), name='crear_item'),
    path('editar_item/<int:pk>', login_required(ActualizarItem.as_view()), name='editar_item'),
    path('eliminar_item/<int:pk>', login_required(EliminarItem.as_view()), name='eliminar_item'),

    path('listar_categoria/', login_required(ListadoCategoria.as_view()), name='listar_categoria'),
    path('crear_categoria/', login_required(CrearCategoria.as_view()), name='crear_categoria'),
    path('editar_categoria/<int:pk>', login_required(ActualizarCategoria.as_view()), name='editar_categoria'),
    path('eliminar_categoria/<int:pk>', login_required(EliminarCategoria.as_view()), name='eliminar_categoria'),

    path('listar_proyecto/', login_required(ListadoProyecto.as_view()), name='listar_proyecto'),
    path('crear_proyecto/', login_required(CrearProyecto.as_view()), name='crear_proyecto'),
    path('editar_proyecto/<int:pk>', login_required(ActualizarProyecto.as_view()), name='editar_proyecto'),
    path('eliminar_proyecto/<int:pk>', login_required(EliminarProyecto.as_view()), name='eliminar_proyecto'),

    path('listar_imagen/', login_required(ListadoImagen.as_view()), name='listar_imagen'),
    path('crear_imagen/', login_required(CrearImagen.as_view()), name='crear_imagen'),
    path('editar_imagen/<int:pk>', login_required(ActualizarImagen.as_view()), name='editar_imagen'),
    path('eliminar_imagen/<int:pk>', login_required(EliminarImagen.as_view()), name='eliminar_imagen'),

    path('listar_comentario/', login_required(ListadoComentario.as_view()), name='listar_comentario'),
    path('eliminar_comentario/<int:pk>', login_required(EliminarComentario.as_view()), name='eliminar_comentario'),

    path('listar_interesado/', login_required(ListadoInteresado.as_view()), name='listar_interesado'),
    path('eliminar_interesado/<int:pk>', login_required(EliminarInteresado.as_view()), name='eliminar_interesado'),

    path('listar_suscriptor/', login_required(ListadoSuscriptor.as_view()), name='listar_suscriptor'),
    path('eliminar_suscriptor/<str:pk>', login_required(EliminarSuscriptor.as_view()), name='eliminar_suscriptor'),

]