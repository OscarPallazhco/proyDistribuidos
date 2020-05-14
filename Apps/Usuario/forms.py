from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuario

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'input100'
        self.fields['username'].widget.attrs['type'] = 'text'
        self.fields['password'].widget.attrs['class'] = 'input100'
        self.fields['password'].widget.attrs['type'] = 'password'

class FormularioUsuario(forms.ModelForm):
    """Variables password1: Contraseña
                password2: Contraseña de Verificación."""

    password1 = forms.CharField(label='Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Ingrese su contraseña',
            'id' : 'password1',
            'required' : 'required',
        }
    ))
    password2 = forms.CharField(label='Contraseña de Confirmación', widget = forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Ingrese su contraseña de nuevo',
            'id' : 'password2',
            'required' : 'required',
        }
    ))

    class Meta:
        model = Usuario
        fields = ('username','email','nombres','apellidos', 'usuario_activo', 'usuario_administrador')
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico del usuario',
            'nombres': 'Nombres del usuario',
            'apellidos': 'Apellidos del usuario',
            'usuario_activo' : 'Estado del usuario',
            'usuario_administrador': 'Condición de Administrador'
        }
        widgets = {
            'username': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre de usuario',
                }
            ),
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese su correo electrónico',
                }
            ),            
            'nombres': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                }
            ),
            'apellidos': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese sus apellidos',
                }                
            ),
            'usuario_activo': forms.CheckboxInput(
                attrs = {
                    'class': 'form-control',
                }                
            ),
            'usuario_administrador': forms.CheckboxInput(
                attrs = {
                    'class': 'form-control',
                }                
            )
        }

    def clean_password(self):
        '''
            Método de validación para hacer que las contraseñas coincidan antes de ser encriptadas y enviarla a la base de datos
            Si las contraseñas no coinciden mostrarán un ValidationError
        '''
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden!')
        return password2

    def save(self,commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user