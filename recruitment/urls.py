from django.urls import path
from . import views

urlpatterns = [
    path('join-us/', views.recruit_view, name='join_us'),
] 