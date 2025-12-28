from django.urls import path
from . import views
appName = "apptareas"
urlpatterns = [
    path("", views.index, name="index"),
    path("tasks/<int:id>/", views.detail, name="detail"),
    path("newTask/", views.create, name = "create"),
    path("tasks/<int:id>/edit/", views.update_task, name="update_task"),
    path("tasks/<int:id>/delete/", views.delete_task, name="delete_task")
]