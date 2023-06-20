from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    fecha_prestamo = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Prestamo
        fields = ['libro', 'cliente', 'fecha_prestamo','fecha_devolucion']

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        del self.fields['fecha_devolucion']