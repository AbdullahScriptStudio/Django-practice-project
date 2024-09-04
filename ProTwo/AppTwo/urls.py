from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home page'),
    path('help/', views.help, name='help page'),
    path('about/', views.about, name='about page'),   
]
