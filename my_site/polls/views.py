from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Teacher, Group
from .forms import TeacherForm, GroupForm


def index(request):
    return HttpResponse("You are here")


def add_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/teachers/")
    else:
        t = Teacher.objects.last()
        form = TeacherForm(instance=t)
        return render(request, "teacher.html", {"form": form})


def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers.html", {"teachers": teachers})


def add_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect("/groups/")
    else:
        g = Group.objects.last()
        form = GroupForm(instance=g)
        return render(request, "group.html", {"form": form})


def groups(request):
    groups = Group.objects.all()
    return render(request, "groups.html", {"groups": groups})
