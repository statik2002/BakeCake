
from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/<slug:slug>', views.show_catalog, name='show_catalog')
]
