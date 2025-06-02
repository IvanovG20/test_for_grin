from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload'),
    path('albums/', views.album_list, name='album_list'),
    path('albums/data/', views.album_data, name='album_data'),
]
