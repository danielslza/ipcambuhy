from django.contrib import admin
from django.urls import path
from membros.api import api

urlpatterns = [
    path('admin/', admin.site.urls), # Corrigido aqui!
    path("api/", api.urls),
]