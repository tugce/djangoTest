from django import forms

from .models import Wsdl

class WsdlForm(forms.ModelForm):

    class Meta:
        model = Wsdl
        fields = ('name',)
