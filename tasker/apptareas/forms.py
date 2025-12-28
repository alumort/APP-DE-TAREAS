from django import forms
from .models import Task, Page

class NewTask(forms.Form):
    taskname = forms.CharField(label= "Task name: ", max_length = 100)
    taskdescription = forms.CharField(label = "Description and status(finished/todo/in progress)): ", max_length = 400, required=False)
    tasklist = forms.ModelChoiceField(
        queryset=Page.objects.all(),
        required = True
    )
