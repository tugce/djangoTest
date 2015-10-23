from django.shortcuts import render
from .models import Wsdl, Method
from suds.client import Client
# Create your views here.
def get_wsdl(request):
    return render(request, 'owscall/get_wsdl.html', {})
