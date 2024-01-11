from django.shortcuts import render,redirect
from .forms import TaskForm
# Create your views here.


def add_task(req):
    if req.method == "POST":
        form = TaskForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
        return redirect("homepage")
    else:
        form = TaskForm()
    return render(req, 'add_task.html', {'form':form})