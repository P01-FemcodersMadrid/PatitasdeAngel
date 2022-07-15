from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.forms import ModelForm
from academiapp.models import *
from django.contrib.auth.models import User

class MascotaForm(ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__'

"""
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }
"""
#	class RegistroForm(UserCreationForm):
#		password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
#		password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

#		class Meta:
#			model = Cuenta
#			fields = ('email', 'username', 'password1', 'password2')
#			label = {'username': 'Nombre completo', 'email': 'Coloca un email'}
#			# help_texts = {k:"" for k in fields }

#	class AutenticarForm(forms.ModelForm):

#		password = forms.CharFiel(label='Contraseña', widget=forms.PasswordInput)

#	class Meta:
#			model = Cuenta
#			fields = ('email', 'password')

#		def clean(self):
#			email = self.cleaned_data['email']
#			password = self.cleaned_data['password']

#			if not authenticate(email=email, password=password):
#				raise forms.ValidationError('El email o contraseña son incorrectos')











