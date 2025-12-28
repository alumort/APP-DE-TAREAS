from django.shortcuts import get_object_or_404, render, redirect
from apptareas.models import Task
from .forms import NewTask
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator


def index(request):
    latest_task_list = Task.objects.order_by("-lastModified")
    paginator = Paginator(latest_task_list, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj
    }
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
            tasklist = form.cleaned_data["tasklist"]
            Task.objects.create(taskname=taskname, taskdescription= taskdescription, tasklist = tasklist)
            return redirect("index")

    else:
        form = NewTask()
    
    return render(request, "apptareas/new_task.html", {
        "form": form
    })

def update_task(request, id):
    task = get_object_or_404(Task, pk=id)

    if request.method == "POST":
        form = NewTask(request.POST)
        if form.is_valid():
            task.taskname = form.cleaned_data["taskname"]
            task.taskdescription = form.cleaned_data["taskdescription"]
            task.tasklist = form.cleaned_data["tasklist"]
            task.save()  
            return redirect("index")
    else:
        form = NewTask(initial={
            "taskname": task.taskname,
            "taskdescription": task.taskdescription,
            "tasklist": task.tasklist
        })

    return render(request, "apptareas/update_task.html", {"form": form, "task": task})


def delete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == "POST":
        task.delete()
        return redirect("index")
    return render(request, "apptareas/delete_task.html", {"task": task})