from django.contrib import admin
from .models import Cliente, Interesado, Suscriptor, Categoria, Proyecto, Imagen, Comentario, Item, Cotizacion


# Register your models here.
admin.site.register(Cliente)
admin.site.register(Interesado)
admin.site.register(Suscriptor)
admin.site.register(Categoria)
admin.site.register(Proyecto)
admin.site.register(Imagen)
admin.site.register(Comentario)
admin.site.register(Item)
admin.site.register(Cotizacion)