from django.contrib import admin
from django.urls import path

from file_manager.views import file_list, file_upload

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', file_upload, name='file_upload'),
    path('files/', file_list, name='file_list')
]
