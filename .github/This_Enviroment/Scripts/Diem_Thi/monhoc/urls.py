from django.urls import path
from . import views

urlpatterns = [
    path('monhoc/', views.monhoc, name='monhoc'),
]