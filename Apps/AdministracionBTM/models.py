from django.db import models

class Categoria(models.Model):
    idcateg = models.AutoField(primary_key=True, verbose_name='ID')
    tag = models.CharField(max_length=20, verbose_name='Tag')
    nombre = models.CharField(max_length=50, verbose_name='Nombre de Categoría')
    descripcion = models.TextField(null=True, blank=True, verbose_name='Descripción')
    sourceimg = models.CharField(max_length=100, verbose_name='Imagen de Categoría')
    estado = models.BooleanField(default=True, verbose_name='Estado')
    createdat = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updatedat = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')
    #deletedat = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categoria'
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'
        ordering = ['createdat']

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    ci_ruc = models.CharField(primary_key=True, max_length=13, verbose_name='Cédula de Identidad/RUC')
    nombres = models.CharField(max_length=50, verbose_name='Nombres')
    apellidos = models.CharField(max_length=50, verbose_name='Apellidos')
    telefono = models.CharField(max_length=20, default="0999999999", verbose_name='Teléfono')
    empresa = models.CharField(max_length=50, blank=True, null=True, verbose_name='Empresa')
    web = models.URLField(max_length=200, blank=True, null=True, verbose_name='Página Web')
    direccion = models.CharField(max_length=50, verbose_name='Dirección', null=True, blank=True)
    provincia = models.CharField(max_length=50, verbose_name='Provincia', null=True, blank=True)
    canton = models.CharField(max_length=50, verbose_name='Cantón', null=True, blank=True)
    cp = models.CharField(max_length=6, null=True, blank=True, verbose_name='Código Postal')
    correo = models.EmailField(max_length=254, verbose_name='Correo Electrónico')      
    descripcion = models.TextField(null=True, blank=True, verbose_name='Descripción')
    notas = models.CharField(max_length=500, null=True, blank=True, verbose_name='Notas') 
    disponibilidad = models.BooleanField(default=True, verbose_name='Disponibilidad')   
    createdat = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updatedat = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')
    #deletedat = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cliente'
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
        ordering = ['-createdat']

    def __str__(self):
        return '%s %s' % (self.nombres, self.apellidos)

class Proyecto(models.Model):
    idproy = models.AutoField(primary_key=True, verbose_name='ID')
    nombre = models.CharField(max_length=50, verbose_name='Nombre del Proyecto')
    descripcion = models.TextField(verbose_name='Descripción')
    idcateg = models.ForeignKey(Categoria, db_column='idcateg', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Categoría')
    ci_ruc = models.ForeignKey(Cliente, db_column='ci_ruc', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Cliente')
    sourceimg = models.CharField(max_length=200, null=True, blank=True, verbose_name='Imagen del Proyecto')
    estado = models.BooleanField(default=True, verbose_name='Estado')
    createdat = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updatedat = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')
    #deletedat = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'proyecto'
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['createdat']

    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    idcomentario = models.AutoField(primary_key=True, verbose_name='ID')
    correo = models.EmailField(max_length=254, verbose_name='Correo Electrónico')
    nombres = models.CharField(max_length=50, null=True, blank=True, verbose_name='Nombres')
    apellidos = models.CharField(max_length=50, null=True, blank=True, verbose_name='Apellidos')
    comentario = models.TextField(null=True, blank=True, verbose_name='Mensaje')
    idproy = models.ForeignKey(Proyecto, null=True, blank=True, db_column='idproy', on_delete=models.CASCADE, verbose_name='Proyecto')
    estado = models.BooleanField(default=True, verbose_name='Estado')
    createdat = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updatedat = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')
    #deletedat = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comentario'
        verbose_name = 'comentario'
        verbose_name_plural = 'comentarios'
        ordering = ['createdat']

    def __str__(self):
        return self.correo

class Item(models.Model):
    iditem = models.AutoField(primary_key=True, verbose_name='ID')
    nombre = models.CharField(max_length=50, verbose_name='Nombre del producto')    
    cantidad = models.IntegerField(verbose_name='Cantidad')
    preciounit = models.FloatField(verbose_name='Precio Unitario')
    descripcion = models.TextField(verbose_name='Descripción', null=True, blank=True)
    estado = models.BooleanField(default=True, verbose_name='Estado')
    createdat = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updatedat = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')
    #deletedat = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'item'
        verbose_name = 'ítem'
        verbose_name_plural = 'ítems'
        ordering = ['createdat']

    def __str__(self):
        return str(self.cantidad)+" |"+self.nombre+" |$"+str(self.preciounit)


class Cotizacion(models.Model):
    idcot = models.AutoField(primary_key=True, verbose_name='ID')
    ci_ruc = models.ForeignKey(Cliente, db_column='ci_ruc', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Cliente')
    motivo = models.CharField(max_length=100, verbose_name='Motivo')
    iditem = models.ManyToManyField(Item)
    condicionpago = models.CharField(max_length=100, verbose_name='Condición de Pago')
    tiempoestimado = models.CharField(max_length=100, verbose_name='Tiempo Estimado')
    estado = models.BooleanField(default=True, verbose_name='Estado')
    createdat = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updatedat = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')
    #deletedat = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cotizacion'
        verbose_name = 'cotización'
        verbose_name_plural = 'cotizaciones'
        ordering = ['createdat']

    def __str__(self):
        return self.motivo

class Imagen(models.Model):
    idimagen = models.AutoField(primary_key=True, verbose_name='ID')
    pathimg = models.CharField(max_length=100, verbose_name='Path')
    descripcion = models.TextField(null=True, blank=True, verbose_name='Descripción')
    idproy = models.ForeignKey(Proyecto, db_column='idproy', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Proyecto')
    estado = models.BooleanField(default=True, verbose_name='Estado')
    createdat = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updatedat = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')
    #deletedat = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'imagen'
        verbose_name = 'imagen'
        verbose_name_plural = 'imágenes'
        ordering = ['createdat']

    def __str__(self):
        return self.pathimg

class Interesado(models.Model):
    idinteresado = models.AutoField(primary_key=True, verbose_name='ID')
    nombres = models.CharField(max_length=50, null=True, blank=True, verbose_name='Nombres')
    apellidos = models.CharField(max_length=50, null=True, blank=True, verbose_name='Apellidos')
    correo = models.EmailField(max_length=254, verbose_name='Correo Electrónico')
    asunto = models.CharField(max_length=50, verbose_name='Asunto')
    mensaje = models.TextField(verbose_name='Mensaje')
    estado = models.BooleanField(default=True, verbose_name='Estado')
    createdat = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updatedat = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')
    #deletedat = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'interesado'
        verbose_name = 'interesado'
        verbose_name_plural = 'interesados'
        ordering = ['createdat']

    def __str__(self):
        return self.correo

class Suscriptor(models.Model):
    correo = models.EmailField(primary_key=True, max_length=254, verbose_name='Correo electrónico')
    estado = models.BooleanField(default=True, verbose_name='Estado')
    createdat = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updatedat = models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')
    #deletedat = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'suscriptor'
        verbose_name = 'suscriptor'
        verbose_name_plural = 'suscriptores'
        ordering = ['-createdat']

    def __str__(self):
        return self.correo
