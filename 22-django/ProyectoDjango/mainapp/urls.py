from django.urls import path
#import views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('inicio/', views.index, name="inicio"),
    path('registro/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout")
]
