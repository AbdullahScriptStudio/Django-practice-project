from django.urls import path
from . import views

# TEMPLATE_TAGGING
app_name = 'app2'


urlpatterns = [
    path('', views.home, name = 'home2'),
    path('users/', views.users_page, name='users_page'),
    path('contact/', views.contact_page, name='contact2'),
    path('launching_soon/', views.launching_page, name ='launching2'),
    path('test/', views.test, name='test'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
]
