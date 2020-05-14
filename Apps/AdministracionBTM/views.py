from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from .forms import *
from .models import *

# Create your views here.

class Inicio(TemplateView):
    """Clase que renderiza el index del sistema"""
    template_name ='index.html'

class ListadoCliente(View):
    """Contiene la lógica para el listado de autores.
    :parámetro model: Modelo a utilizarse
    :type model: Model
    :parámetro form_class: Form de Django referente a model
    :type form_class: DjangoForm
    :parámetro template_name: Template a utilizarse en la clase
    :type template_name: str"""

    model = Cliente
    form_class = ClienteForm
    template_name = 'AdministracionBTM/cliente/listar_cliente.html'

    def get_queryset(self):
        """Retorna una consulta a utilizarse en la clase.
        Esta funcion se encuentra en toda vista basada en  clase, se utiliza internamente por django para
        generar las consultas de a cuerdo a los valores que se definen en la clase, valores como MODEL,FORM_CLASS
        :return: una consulta
        :rtype: Queryset"""

        return self.model.objects.filter(disponibilidad=True)

    def get_context_data(self, **kwargs):
        """Retorna un contexto a enviar a template.
        Aquí definimos todas las variables que necesitamos enviar a nuestro template definido en TEMPLATE_NAME,
        se agregan a un diccionario general para poder ser enviados en la funcion RENDER.
        :return: un contexto
        :rtype: dict"""

        contexto = {}
        contexto['clientes'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto

    def get(self, request, *args, **kwargs):
        """Renderiza un template con un contexto dado.
        Se encarga de manejar toda petición enviada del navegador a Django a través del método GET
        del protocolo HTTP, en este caso renderiza un template definido en TEMPLATE_NAME junto con
        el contexto definido en GET_CONTEXT_DATA.
        :return: render
        :rtype: func"""

        return render(request, self.template_name, self.get_context_data())

class ActualizarCliente(UpdateView):
    """Contiene la lógica para edición de un Cliente
    :parámetro model: Modelo a utilizarse
    :type model: Model
    :parámetro form_class: Form de Django referente a model
    :type form_class: DjangoForm
    :parámetro template_name: Template a utilizarse en la clase
    :type template_name: str
    :parámetro success_url: Url de redireccionado al actualizar
    :type success_url: URL
    """
    model = Cliente
    template_name = 'AdministracionBTM/cliente/cliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('AdministracionBTM:listar_cliente')

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['clientes'] = Cliente.objects.filter(disponibilidad=True)
        return context

class CrearCliente(CreateView):
    """Contiene la lógica para crear un Cliente
    :parámetro model: Modelo a utilizarse
    :type model: Model
    :parámetro form_class: Form de Django referente a model
    :type form_class: DjangoForm
    :parámetro template_name: Template a utilizarse en la clase
    :type template_name: str
    :parámetro success_url: Url de redireccionado al actualizar
    :type success_url: URL """
    model = Cliente
    template_name = 'AdministracionBTM/cliente/crear_cliente.html'
    form_class = ClienteForm
    success_url = reverse_lazy('AdministracionBTM:listar_cliente')

class EliminarCliente(DeleteView):
    """Elimina logicamente un objeto.
        Se encarga de manejar las peticiones de tipo POST enviadas del navegador a Django.
        :parámetro pk: clave primaria
        :type pk: int
        :parámetro request: petición enviada del navegador
        :type request: request
        :return: redirect
        :rtype: func  """
    model = Cliente
    def post(self, request, pk, *args, **kwargs):
        object = Cliente.objects.get(ci_ruc=pk)
        object.disponibilidad = False
        object.save()
        return redirect('AdministracionBTM:listar_cliente')

class ListadoCotizacion(View):
    model = Cotizacion
    form_class = CotizacionForm
    template_name = 'AdministracionBTM/cotizacion/listar_cotizacion.html'

    def get_queryset(self):
        return self.model.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['cotizaciones'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

class CrearCotizacion(CreateView):
    model= Cotizacion
    template_name = 'AdministracionBTM/cotizacion/crear_cotizacion.html'
    form_class = CotizacionForm
    success_url = reverse_lazy('AdministracionBTM:listar_cotizacion')

class ActualizarCotizacion(UpdateView):
    model = Cotizacion
    template_name = 'AdministracionBTM/cotizacion/cotizacion.html'
    form_class = CotizacionForm
    success_url = reverse_lazy('AdministracionBTM:listar_cotizacion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cotizaciones'] = Cotizacion.objects.filter(estado=True)
        return context

class EliminarCotizacion(DeleteView):
    model = Cotizacion
    def post(self, request, pk, *args, **kwargs):
        object = Cotizacion.objects.get(idcot=pk)
        object.estado = False
        object.save()
        return redirect('AdministracionBTM:listar_cotizacion')

class ListadoItem(View):
    model = Item
    form_class = ItemForm
    template_name = 'AdministracionBTM/item/listar_item.html'

    def get_queryset(self):
        return self.model.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['items'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

class CrearItem(CreateView):
    model = Item
    template_name = 'AdministracionBTM/item/crear_item.html'
    form_class = ItemForm
    success_url = reverse_lazy('AdministracionBTM:listar_item')

class ActualizarItem(UpdateView):
    model = Item
    template_name = 'AdministracionBTM/item/item.html'
    form_class = ItemForm
    success_url = reverse_lazy('AdministracionBTM:listar_item')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.filter(estado=True)
        return context

class EliminarItem(DeleteView):
    model = Item
    def post(self, request, pk, *args, **kwargs):
        object = Item.objects.get(iditem=pk)
        object.estado = False
        object.save()
        return redirect('AdministracionBTM:listar_item')

class ListadoCategoria(View):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'AdministracionBTM/categoria/listar_categoria.html'

    def get_queryset(self):
        return self.model.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['categorias'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

class CrearCategoria(CreateView):
    model = Categoria
    template_name = 'AdministracionBTM/categoria/crear_categoria.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('AdministracionBTM:listar_categoria')

class ActualizarCategoria(UpdateView):
    model = Categoria
    template_name = 'AdministracionBTM/categoria/categoria.html'
    form_class = CategoriaForm
    success_url = reverse_lazy('AdministracionBTM:listar_categoria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.filter(estado=True)
        return context

class EliminarCategoria(DeleteView):
    model = Categoria
    def post(self, request, pk, *args, **kwargs):
        object = Categoria.objects.get(idcateg=pk)
        object.estado = False
        object.save()
        return redirect('AdministracionBTM:listar_categoria')

class ListadoProyecto(View):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'AdministracionBTM/proyecto/listar_proyecto.html'

    def get_queryset(self):
        return self.model.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['proyectos'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

class CrearProyecto(CreateView):
    model = Proyecto
    template_name = 'AdministracionBTM/proyecto/crear_proyecto.html'
    form_class = ProyectoForm
    success_url = reverse_lazy('AdministracionBTM:listar_proyecto')

class ActualizarProyecto(UpdateView):
    model = Proyecto
    template_name = 'AdministracionBTM/proyecto/proyecto.html'
    form_class = ProyectoForm
    success_url = reverse_lazy('AdministracionBTM:listar_proyecto')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proyectos'] = Proyecto.objects.filter(estado=True)
        return context

class EliminarProyecto(DeleteView):
    model = Proyecto
    def post(self, request, pk, *args, **kwargs):
        object = Proyecto.objects.get(idproy=pk)
        object.estado = False
        object.save()
        return redirect('AdministracionBTM:listar_proyecto')

class ListadoImagen(View):
    model = Imagen
    form_class = ImagenForm
    template_name = 'AdministracionBTM/imagen/listar_imagen.html'

    def get_queryset(self):
        return self.model.objects.filter(estado=True)

    def get_context_data(self, **kwargs):
        contexto = {}
        contexto['imagenes'] = self.get_queryset()
        contexto['form'] = self.form_class
        return contexto

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

class CrearImagen(CreateView):
    model = Imagen
    template_name = 'AdministracionBTM/imagen/crear_imagen.html'
    form_class = ImagenForm
    success_url = reverse_lazy('AdministracionBTM:listar_imagen')

class ActualizarImagen(UpdateView):
    model = Imagen
    template_name = 'AdministracionBTM/imagen/imagen.html'
    form_class = ImagenForm
    success_url = reverse_lazy('AdministracionBTM:listar_imagen')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['imagenes'] = Imagen.objects.filter(estado=True)
        return context

class EliminarImagen(DeleteView):
    model = Imagen
    def post(self, request, pk, *args, **kwargs):
        object = Imagen.objects.get(idimagen=pk)
        object.estado = False
        object.save()
        return redirect('AdministracionBTM:listar_imagen')

class ListadoComentario(ListView):
    model = Comentario
    template_name = 'AdministracionBTM/comentario/listar_comentario.html'
    context_object_name = 'comentarios'
    queryset = Comentario.objects.filter(estado=True)

class EliminarComentario(DeleteView):
    model = Comentario
    def post(self, request, pk, *args, **kwargs):
        object = Comentario.objects.get(idcomentario=pk)
        object.estado = False
        object.save()
        return redirect('AdministracionBTM:listar_comentario')

class ListadoInteresado(ListView):
    model = Interesado
    template_name = 'AdministracionBTM/interesado/listar_interesado.html'
    context_object_name = 'comentarios'
    queryset = Interesado.objects.filter(estado=True)

class EliminarInteresado(DeleteView):
    model = Interesado
    def post(self, request, pk, *args, **kwargs):
        object = Interesado.objects.get(idinteresado=pk)
        object.estado = False
        object.save()
        return redirect('AdministracionBTM:listar_interesado')

class ListadoSuscriptor(ListView):
    model = Suscriptor
    template_name = 'AdministracionBTM/suscriptor/listar_suscriptor.html'
    context_object_name = 'suscriptores'
    queryset = Suscriptor.objects.filter(estado=True)

class EliminarSuscriptor(DeleteView):
    model = Suscriptor
    def post(self, request, pk, *args, **kwargs):
        object = Suscriptor.objects.get(correo=pk)
        object.estado = False
        object.save()
        return redirect('AdministracionBTM:listar_suscriptor')
