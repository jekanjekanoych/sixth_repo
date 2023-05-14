from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("teacher/", views.add_teacher, name="teacher"),
    path("teachers/", views.teachers, name="teachers"),
    path("group/", views.add_group, name="group"),
    path("groups/", views.groups, name="groups"),
]
