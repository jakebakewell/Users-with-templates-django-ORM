from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_new_user', views.process_new_user)
]