from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Usuario
from .forms import FormularioLogin, FormularioUsuario

class Login(FormView):
    template_name = 'login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        login(self.request,form.get_user())
        return super(Login,self).form_valid(form)

def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

class ListarUsuario(ListView):
    model = Usuario
    template_name = "usuarios/listar_usuario.html"
    context_object_name = 'usuarios'

    def get_queryset(self):
        return self.model.objects.filter(usuario_activo=True)


class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuarios/crear_usuario.html'

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            nuevousuario = Usuario (
                email = form.cleaned_data.get('email'),
                username = form.cleaned_data.get('username'),
                nombres = form.cleaned_data.get('nombres'),
                apellidos = form.cleaned_data.get('apellidos'),
                usuario_activo = form.cleaned_data.get('usuario_activo'),
                usuario_administrador = form.cleaned_data.get('usuario_administrador')
            )
            nuevousuario.set_password(form.cleaned_data.get('password1'))
            nuevousuario.save()
            return redirect('Usuario:listar_usuario')
        else:
            return render(request, self.template_name, {'form': form})

class ActualizarUsuario(UpdateView):
    model = Usuario
    template_name = 'usuarios/usuario.html'
    form_class = FormularioUsuario
    success_url = reverse_lazy('Usuario:listar_usuario')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuarios'] = Usuario.objects.filter(usuario_activo=True)
        return context

class EliminarUsuario(DeleteView):
    model = Usuario
    def post(self, request, pk, *args, **kwargs):
        object = Usuario.objects.get(username=pk)
        object.usuario_activo = False
        object.save()
        return redirect('Usuario:listar_usuario')