from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('certification-body/', views.certification_body, name='certification_body'),
    path('testing-laboratory/', views.testing_laboratory, name='testing_laboratory'),
]
