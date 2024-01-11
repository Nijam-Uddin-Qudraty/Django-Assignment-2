from django.shortcuts import redirect,render
from task.models import TaskModel
from task.forms import TaskForm
from category.models import TaskCategory
from category.forms import CategoryForm
def home(req):
    return render(req, 'base.html')


def show_task(req):
    form = TaskModel.objects.all()
    return render(req, 'show_task.html',{'form':form})

def edit(req,id):
    task = TaskModel.objects.get(pk=id)
    form = TaskForm(instance=task)
    if req.method == "POST":
        form = TaskForm(req.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect("show_task")
    return render(req,"add_task.html",{'form':form})
def delete(req,id):
    task = TaskModel.objects.get(pk=id).delete()
    return redirect("show_task")
