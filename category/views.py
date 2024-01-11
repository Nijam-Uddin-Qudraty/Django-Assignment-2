
from django.shortcuts import render, redirect
from .forms import CategoryForm
# Create your views here.


def add_category(req):
    if req.method == "POST":
        form = CategoryForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
        return redirect("homepage")
    else:
        form = CategoryForm()
    return render(req, 'add_category.html', {'form': form})
