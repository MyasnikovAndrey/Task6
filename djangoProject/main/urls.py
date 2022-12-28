from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('loading/', views.loading_page, name = 'loading_page'),
    path ('loading/main/',views.abobus, name = "abobus"),
]
