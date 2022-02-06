from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home-page'),
    path('file_system', views.file_system, name='file_system'),
    path('signup', views.signup, name='signup'),
]