from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vojaci/', views.VojaciListView.as_view(), name='soldiers'),
    path('vojaci/<int:pk>/', views.VojaciDetailView.as_view(), name='podrobnosti'),
]