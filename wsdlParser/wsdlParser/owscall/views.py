from django.shortcuts import render, get_object_or_404
from .models import Wsdl, Method
from django.shortcuts import redirect
from .forms import WsdlForm
from suds.client import Client
import logging.config
# Create your views here.
def wsdl_list(request):
    wsdls = Wsdl.objects.all()
    print wsdls
    return render(request, 'owscall/wsdl_list.html', {'wsdls': wsdls})
def wsdl_detail(request, pk):
    wsdl = get_object_or_404(Wsdl, pk=pk)
    return render(request, 'owscall/wsdl_detail.html', {'wsdl': wsdl})
def wsdl_new(request):
    if request.method == "POST":
        form = WsdlForm(request.POST)
        if form.is_valid():
            wsdl = form.save(commit=False)
            wsdl.name = form.cleaned_data['name']
            print wsdl.name
            client = Client(wsdl.name)
            wsdl.save()
            for method in client.wsdl.services[0].ports[0].methods.values():
                methodW = Method()
                methodW.wsdlId = wsdl
                methodW.name = method.name
                methodW.paremeters = method.soap.input.body.parts
                print 'Method name = ', method.name
                print 'Method parameters = ', methodW.paremeters
                methodW.save()

            return redirect('owscall.views.wsdl_detail', pk=wsdl.pk)
    else:
        form = WsdlForm()
    return render(request, 'owscall/wsdl_edit.html', {'form': form})
def wsdl_edit(request, pk):
    wsdl = get_object_or_404(Wsdl, pk=pk)
    if request.method == "POST":
        form = WsdlForm(request.POST, instance=wsdl)
        if form.is_valid():
            wsdl = form.save(commit=False)
            wsdl.name = form.cleaned_data['name']
            wsdl.save()
            return redirect('owscall.views.wsdl_detail', pk=wsdl.pk)
    else:
        form = WsdlForm(instance=wsdl)
    return render(request, 'owscall/wsdl_edit.html', {'form': form})
def method_list(request, wsdl_id):
    print "pk ===== ", pk
    wsdl = Wsdl.objects.filter(id=wsdl_id)
    methods = Method.objects.filter(wsdlId=wsdl)
    return render(request, 'owscall/method_list.html', {'methods': methods})
def method_detail(request, pk):
    method = get_object_or_404(Method, pk=pk)
    return render(request, 'owscall/method_detail.html', {'method': method})
