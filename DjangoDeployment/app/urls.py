# Standard Django imports for url allocation
from django.urls import include, path
from app import views

# urls

urlpatterns = [
    path("home/", views.homePage, name="home"),
    path("predict/", views.predictPage, name="predict")
]
