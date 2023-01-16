from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('list_of_tasks.urls', namespace='home')),
    path('admin/', admin.site.urls),
]
