from django import forms

#from .models import Participant

#opção simples automatico do python
"""class RegistrationForm(forms.ModelForm):   #isso vai gerar os formulários. Devemos passá-los para as vies
    class Meta:
        model = Participant
        fields = ['email']"""

class RegistrationForm(forms.Form):   #isso vai gerar os formulários. Devemos passá-los para as vies
    email = forms.EmailField(label='Your email')
