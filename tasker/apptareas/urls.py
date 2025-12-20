from django.urls import path
from . import views
appName = "apptareas"
urlpatterns = [
    path("", views.index, name="index"),
    path("tasks/<int:id>/", views.detail, name="detail"),
    path("newTask/", views.create, name = "create")
]