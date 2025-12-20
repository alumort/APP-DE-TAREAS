from django.shortcuts import get_object_or_404, render, redirect
from apptareas.models import Task
from .forms import NewTask
from django.http import HttpResponseRedirect

def index(request):
    latest_task_list = Task.objects.order_by("-lastModified")[:5]
    context = {"latest_task_list": latest_task_list}
    return render(request, "apptareas/index.html", context)

def detail(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, "apptareas/detail.html", {"task": task})

def create(request):
    if request.method == "POST":
        form = NewTask(request.POST)
        if form.is_valid():
            taskname = form.cleaned_data["taskname"]
            taskdescription = form.cleaned_data["taskdescription"]
            task = Task.objects.create(taskname=taskname, taskdescription= taskdescription)
            return redirect("index()")
    else:
        form = NewTask()
    return render(request, "apptareas/create.html", {"form": form})

#se duplica newTask/newTask cuando se mandan 2 veces el formulario de cerar tareas