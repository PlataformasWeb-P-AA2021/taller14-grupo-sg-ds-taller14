from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Edificio, Departamento

# Form Edificio
class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese el nombre del Edificio por favor'),
            'direccion': _('Ingrese la direccion por favor'),
            'ciudad': _('Ingrese la ciudad por favor'),
            'tipo': _('Ingrese el tipo de Edificio por favor'),
        }

# Form Departamento   
class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['propietario', 'costo', 'numCuartos', 'edificio']
    
  
# Form DepartamentoEdificio
class DepartamentoEdificioForm(ModelForm):
    
    def __init__(self, edificio, *args, **kwargs):
        super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        print(edificio)

    class Meta:
        model = Departamento
        fields = ['propietario', 'costo', 'numCuartos', 'edificio']
   
    