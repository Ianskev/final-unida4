from django import forms
from django.contrib.auth.models import User

class ProyectoForm(forms.Form):
    foto=forms.URLField(label="Foto: ")
    titulo_proyecto= forms.CharField(label="Título del Proyecto: ")
    descripcion=forms.CharField(widget=forms.Textarea)
    tags=forms.CharField(label="Tags: ")
    url_github=forms.URLField()
    autor = forms.ModelChoiceField(label="autor", queryset=User.objects.all())