from django.urls import path
from . import views

urlpattern = [
    path('paints/<int:pk>/', views.paints),
]