from django.urls import path
from . import views


app_name = 'skating'
urlpatterns = [
    path('', views.skating, name='skating'),
]
