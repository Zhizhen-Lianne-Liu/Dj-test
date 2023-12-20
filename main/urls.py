#represent the different urls that goes to different views in the view.py file

from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="home")
    
]
