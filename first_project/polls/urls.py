from django.urls import path, include
from . import views
from django.contrib import admin

app_name = 'polls'
urlpatterns = [
    # path('', views.index, name = 'index'),
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name = 'results'),
    # path('question_id/results/', views.results, name = 'results'),
    path('<int:question_id>/vote/', views.vote, name = 'vote'),
]