from django.forms import ModelForm
from .models import ordens_servico

class CadastroForm(ModelForm):
    class Meta:
        model = ordens_servico
        fields = '__all__'