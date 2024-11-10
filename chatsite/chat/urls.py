from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='sobre'),
    path('contact/', views.contact, name='contact'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('success/', views.success, name='success'),
]
