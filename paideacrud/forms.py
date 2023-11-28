from django import forms
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.db.models import ProtectedError

from . import models

class MetaForm(forms.ModelForm):
    class Meta:
        model=models.MetaModelo
        fields=['descripcion','unidad_medida_personas',
                'unidad_medida_evento','meta_programada_evento',
                'meta_realizada_evento','meta_programada_personas',
                'meta_realizada_personas']
    
class TemaForm(forms.ModelForm):
    class Meta:
        model = models.Tema
        fields=['nombre','meta','material','duracion',
                'objetivo'] 
      
class EventoForm(forms.ModelForm):
    class Meta:
        model = models.Evento
        fields=['tema','ubicacion','fecha','material',
                'cant_hombres','cant_mujeres']

class FechaForm(forms.ModelForm):
    class Meta:
        model = models.getFecha
        fields=['fecha_inicio','fecha_fin','tipo']