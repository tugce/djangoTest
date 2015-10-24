from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.wsdl_list, name='wsdl_list'),
    url(r'^wsdl/(?P<pk>[0-9]+)/$', views.wsdl_detail, name='wsdl_detail'),
    url(r'^wsdl/new/$', views.wsdl_new, name='wsdl_new'),
    url(r'^wsdl/(?P<pk>[0-9]+)/edit/$', views.wsdl_edit, name='wsdl_edit'),
    url(r'^methods/(?P<wsdl_id>\d+)$', views.method_list, name='method_list'),
    url(r'^method/(?P<pk>[0-9]+)/$', views.method_detail, name='method_detail'),
]
