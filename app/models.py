from django.db import models

# Create your models here.
class Persona(models.Model):
    imagen = models.ImageField(upload_to='', blank=True, null=True)#upload_to='%Y/%m/%d',
    nombre = models.CharField(max_length=45)
    apellidos = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    fecharegistro = models.DateTimeField(auto_now_add=True, blank=True)
    ultimaconexion = models.DateTimeField(auto_now_add=True, blank=True)
    activo = models.BooleanField(blank=True,default=True)
    estado = models.BooleanField(blank=True,default=True)

class Proyecto(models.Model):
    nombre = models.CharField(max_length=45)
    codigo = models.CharField(max_length=45)
    fechacreacion = models.DateTimeField(auto_now_add=True, blank=True)
    estado = models.BooleanField(blank=True,default=True)

class Horaproyecto(models.Model):
    nombre = models.CharField(max_length=45)
    codigo = models.CharField(max_length=45)
    horainicio = models.DateTimeField(auto_now_add=True, blank=True)
    proyecto = models.ForeignKey('Proyecto', on_delete=models.CASCADE)  # Field name made lowercase.
    persona = models.ForeignKey('Persona', on_delete=models.CASCADE)  # Field name made lowercase.
    estado = models.BooleanField(blank=True,default=True)
