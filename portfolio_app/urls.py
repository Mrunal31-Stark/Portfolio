from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('download_resume/', views.download_resume, name='download_resume'),
    path('submit_contact/', views.submit_contact, name='submit_contact'),
]
