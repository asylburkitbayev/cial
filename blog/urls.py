from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('team', views.team, name='team'),
    path('contact', views.contact, name='contact'),
    path('add_email', views.add_email, name='add_email'),
    path('add_contact', views.add_contact, name='add_contact')

]
