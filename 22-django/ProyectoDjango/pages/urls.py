from django.urls import path
#import views
from . import views

urlpatterns = [
    #path('pagina/<str:slug>', pages.views.page, name="page")
    path('pagina/<str:slug>', views.page, name="page")
]
