from django.forms import ModelForm
from .models import ordens_servico,listadeprecos


class CadastroForm(ModelForm):
    class Meta:
        model = ordens_servico
        fields = '__all__'

class ListaDePrecosForm(ModelForm):
    class Meta:
        model =listadeprecos
        fields = '__all__'
