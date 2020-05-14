from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        labels = {
            'ci_ruc': 'Cédula del cliente',
            'nombres': 'Nombres del cliente',
            'apellidos': 'Apellidos del cliente',
            'empresa': 'Empresa del cliente',
            'web': 'Página web del cliente',
            'direccion': 'Dirección del cliente',
            'provincia': 'Provincia del cliente',
            'canton': 'Cantón del cliente',
            'cp': 'Código postal del cliente',
            'correo': 'Correo electrónico del cliente',
            'descripcion': 'Descripción del cliente',
            'notas': 'Notas del cliente',
            'disponibilidad': 'Estado del cliente',
        }
        widgets = {
            'ci_ruc': forms.TextInput(
               attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la cédula del cliente',
                    'id': 'ci_ruc'
               }
            ),
            'nombres': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese los nombres del cliente',
                    'id':'nombres'
                }
            ),
            'apellidos':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese los apellidos del cliente',
                    'id':'apellidos'
                }
            ),
            'empresa': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese la empresa a la que pertenece el cliente',
                    'id':'empresa'
                }
            ),
            'web':forms.URLInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la página web del cliente',
                    'id':'web'
                }
            ),
            'direccion':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la dirección del cliente',
                    'id':'direccion'
                }
            ),
            'provincia':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la provincia del cliente',
                    'id':'provincia'
                }
            ),
            'canton':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el cantón del cliente',
                    'id':'canton'
                }
            ),
            'cp':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el código postal del cliente',
                    'id':'cp'
                }
            ),
            'correo':forms.EmailInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el correo electrónico del cliente',
                    'id':'correo'
                }
            ),
            'descripcion':forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese una descripción del cliente',
                    'id':'descripcion'
                }
            ),
            'notas':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese un dato a recordar del cliente',
                    'id':'notas'
                }
            ),
            'disponibilidad':forms.CheckboxInput(
                attrs = {
                    'class':'form-control',
                    'id':'disponibilidad'
                }
            )
        }


class CotizacionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs): 
        super(CotizacionForm,self).__init__(*args, **kwargs)
        self.fields['ci_ruc'].queryset = Cliente.objects.filter(disponibilidad = True)
        self.fields['iditem'].queryset = Item.objects.filter(estado = True)

    class Meta:
        model = Cotizacion
        fields = ('ci_ruc', 'motivo', 'iditem', 'condicionpago', 'tiempoestimado', 'estado')
        labels = {
            'ci_ruc': 'Cliente',
            'motivo': 'Motivo a cotizar',
            'iditem': 'Productos',
            'condicionpago' : 'Condición de pago',
            'tiempoestimado' : 'Tiempo estimado',
            'estado': 'Estado de la cotización',
        }
        widgets = {
            'ci_ruc': forms.Select(
               attrs = {
                    'class':'form-control',
                    'placeholder':'Seleccione el cliente a cotizar',
                    'id': 'ci_ruc'
               }
            ),
            'motivo': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el motivo de la cotización',
                    'id':'motivo'
                }
            ),
            'iditem': forms.SelectMultiple(
               attrs = {
                    'class':'form-control',
                    'id': 'iditem'
               }
            ),
            'condicionpago':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la condición de pago a establecer',
                    'id':'condicionpago'
                }
            ),
            'tiempoestimado': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder': 'Ingrese el tiempo estimado de desarrollo',
                    'id':'tiempoestimado'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs = {
                    'class':'form-control',
                    'id':'estado'
                }
            )
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('nombre', 'cantidad', 'preciounit', 'descripcion', 'estado')
        labels = {
            'nombre': 'Nombre del Producto',            
            'cantidad': 'Cantidad solicitada del producto',
            'preciounit' : 'Precio unitario del producto',
            'descripcion': 'Descripción del Producto',
            'estado' : 'Estado del producto',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder':'Ingrese el nombre del producto',
                    'id': 'nombre'
                }
            ),            
            'cantidad': forms.NumberInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la cantidad solicitada del producto',
                    'id':'cantidad'
                }
            ),
            'preciounit':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el precio unitario del producto',
                    'id':'condicionpago'
                }
            ),
            'descripcion': forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la descripción del producto',
                    'id':'estado'
                }
            ),
            'estado': forms.CheckboxInput(
                attrs = {
                    'class':'form-control',
                    'id':'estado'
                }
            )
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('tag', 'nombre', 'descripcion', 'sourceimg', 'estado')
        labels = {
            'tag': 'Etiqueta de categoría',
            'nombre': 'Nombre de la categoría',
            'descripcion': 'Descripción de la categoría',
            'sourceimg': 'Imagen de la categoría',
            'estado': 'Estado de la categoría',
        }
        widgets = {
            'tag': forms.TextInput(
               attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la etiqueta de la categoría',
                    'id': 'tag'
               }
            ),
            'nombre':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre de la categoría',
                    'id':'nombre'
                }
            ),
            'descripcion':forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese una descripción de la categoría',
                    'id':'descripcion'
                }
            ),
            'sourceimg':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la ruta de la imagen de la categoría',
                    'id':'sourceimg'
                }
            ),
            'estado':forms.CheckboxInput(
                attrs = {
                    'class':'form-control',
                    'id':'estado'
                }
            )
        }

class ProyectoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs): 
        super(ProyectoForm,self).__init__(*args, **kwargs)
        self.fields['idcateg'].queryset = Categoria.objects.filter(estado = True)
        self.fields['ci_ruc'].queryset = Cliente.objects.filter(disponibilidad = True)
    class Meta:
        model = Proyecto
        fields = ('nombre', 'descripcion', 'idcateg', 'ci_ruc', 'sourceimg', 'estado')
        labels = {
            'nombre': 'Nombre del Proyecto',
            'descripcion': 'Descripción del proyecto',
            'idcateg': 'Categoría del proyecto',
            'ci_ruc': 'Cliente relacionado al proyecto',
            'sourceimg': 'Imagen del proyecto',
            'estado': 'Estado del proyecto',
        }
        widgets = {
            'nombre':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese el nombre del proyecto',
                    'id':'nombre'
                }
            ),
            'descripcion':forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese una descripción del proyecto',
                    'id':'descripcion'
                }
            ),
            'idcateg':forms.Select(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Seleccione la categoría del proyecto',
                    'id':'idcateg'
                }
            ),
            'ci_ruc':forms.Select(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Seleccione el cliente del proyecto',
                    'id':'ci_ruc'
                }
            ),
            'sourceimg':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la ruta de la imagen del proyecto',
                    'id':'sourceimg'
                }
            ),
            'estado':forms.CheckboxInput(
                attrs = {
                    'class':'form-control',
                    'id':'estado'
                }
            )
        }

class ImagenForm(forms.ModelForm):
    def __init__(self, *args, **kwargs): 
        super(ImagenForm,self).__init__(*args, **kwargs)
        self.fields['idproy'].queryset = Proyecto.objects.filter(estado = True)
    class Meta:
        model = Imagen
        fields = ('pathimg', 'descripcion', 'idproy', 'estado')
        labels = {
            'pathimg': 'Ruta de la imagen',
            'descripcion': 'Descripción de la imagen',
            'idproy': 'Proyecto al que pertenece la imagen',
            'estado': 'Estado de la imagen',
        }
        widgets = {
            'pathimg':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la ruta de la imagen',
                    'id':'pathimg'
                }
            ),
            'descripcion':forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese una descripción de la imagen',
                    'id':'descripcion'
                }
            ),
            'idproy':forms.Select(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Seleccione el proyecto',
                    'id':'idproy'
                }
            ),
            'estado':forms.CheckboxInput(
                attrs = {
                    'class':'form-control',
                    'id':'estado'
                }
            )
        }