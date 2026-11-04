from django.contrib import admin
from django.urls import path
from tareas.views import ping

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/ping/", ping)
]