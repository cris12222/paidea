from django.db import models
from safedelete.models import SOFT_DELETE_CASCADE, SafeDeleteModel

#from users.models import AbstractFields

class MetaModelo( SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    descripcion = models.CharField(max_length=255)
    unidad_medida_personas = models.CharField(max_length=255)
    unidad_medida_evento = models.CharField(max_length=255)
    meta_programada_evento = models.IntegerField()
    meta_realizada_evento = models.IntegerField()
    meta_programada_personas = models.IntegerField()
    meta_realizada_personas = models.IntegerField()
    class Meta:
        db_table = 'metas'
        ordering = ['-id']
    def __str__(self):
        return self.descripcion

class Tema( SafeDeleteModel,models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    nombre = models.CharField(max_length=255)
    meta = models.ForeignKey('MetaModelo',on_delete=models.DO_NOTHING,null=True)
    material = models.CharField(max_length=255)
    duracion = models.CharField(max_length=255)
    objetivo = models.CharField(max_length=500)
    class Meta:
        db_table = 'temas'
        ordering = ['id']
    def __str__(self):
        return self.nombre
  
class Evento( SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    tema = models.ForeignKey('Tema',on_delete=models.DO_NOTHING,null=True)
    ubicacion = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    material = models.CharField(max_length=255)
    cant_hombres = models.IntegerField()
    cant_mujeres = models.IntegerField()
    class Meta:
        db_table = 'eventos'
        ordering = ['-id']
    
class getFecha(models.Model):
    fecha_inicio=models.DateField()
    fecha_fin=models.DateTimeField()
    tipo = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.tipo}/{self.fecha_inicio}/{self.fecha_fin}"