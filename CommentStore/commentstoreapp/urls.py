from django.urls import path
from . import views

urlpatterns = [
    path('', views.commentstore, name='commentstoreapp'),
]