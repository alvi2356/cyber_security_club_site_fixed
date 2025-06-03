from django.urls import path
from . import views

app_name = 'former_presidents'

urlpatterns = [
    path('', views.former_presidents_view, name='former_presidents'),
] 