from django import forms
from .models import Teacher, Group


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["first_name", "last_name", "age"]


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["group_name"]
