from django.forms import ModelForm

from .models import Sale

class SaleForm(ModelForm):
    class Meta:
        model = Sale
        fields = (
            'name',
            'city',
            'street',
            'number',
            'cep',
            'state',
        )