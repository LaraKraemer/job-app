from django.urls import path
from . import views

# Import views function
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
]