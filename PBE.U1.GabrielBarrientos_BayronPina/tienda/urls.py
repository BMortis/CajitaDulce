from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('contacto', views.contacto, name= 'contacto'),
    path('home', views.home_template, name= 'home'),
    path('about', views.about_template, name= 'about'),
    #path('about',  TemplateView.as_view(template_name='about.html'), name= 'about')

]