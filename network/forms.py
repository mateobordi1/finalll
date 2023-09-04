from django import forms
from .models import User , Asistencia

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
    
class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        exclude = ['estado']

