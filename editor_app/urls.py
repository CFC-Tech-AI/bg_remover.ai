from django.urls import path
from .views import process_image, download_image

urlpatterns = [
    path('', process_image, name='process_image'),
    path('download/', download_image, name='download_image'),
]
