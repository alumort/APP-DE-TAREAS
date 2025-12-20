from django import forms


class NewTask(forms.Form):
    taskname = forms.CharField(label= "Task name: ", max_length = 100)
    taskdescription = forms.CharField(label = "Description and status(finished/todo/in progress)): ", widget=forms.Textarea)
