
from . import views
from django.urls import include, path
from django.conf.urls.static import static
from kostalek import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('vojaci/', views.VojaciListView.as_view(), name='soldiers'),
    path('vojaci/<int:pk>/', views.VojaciDetailView.as_view(), name='podrobnosti'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)