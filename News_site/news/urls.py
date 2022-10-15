from django.urls import path

from . import views

app_name = 'riddles'
urlpatterns = [
    path(r'', views.index, name='index')
]