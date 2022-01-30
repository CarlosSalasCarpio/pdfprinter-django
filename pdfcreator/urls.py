from django.urls import path
from . import views

app_name = 'pdfcreator'
urlpatterns = [
    path('', views.index, name='index'),
]