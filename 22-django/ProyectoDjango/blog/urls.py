from django.urls import path
#import views
from . import views

urlpatterns = [
    path('articulos/', views.list, name="list_articles")
]
