from django import forms

from .models import Post

class WsdlForm(forms.ModelForm):

    class Meta:
        model = Wsdl
        fields = ('name', 'text',)
