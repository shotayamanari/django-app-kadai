from django.urls import path
from .import views

app_name    = "nagoyameshiapp"
urlpatterns = [
    path("", views.index, name="index")
]