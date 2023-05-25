from django.urls import path, re_path
from django.conf import settings
from . import views

urlpatterns = [
    path('analitics', views.analytics),
    path('diagram', views.diagram),
    path('topclients', views.TopClients)
]