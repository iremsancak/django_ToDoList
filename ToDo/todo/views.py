from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

# Create your views here.
from django.http import HttpResponse
from .models import ListEntry
from .forms import EditForm, CreateForm
def home(request):
    context = {}
    return render(request, 'todo/home.html', context)

def todo_index(request):
    todo_list = ListEntry.objects.order_by('Id')
    context = {
        'todo_list': todo_list,
    }
    return render(request, 'todo/index.html', context)

def todo_delete(request, id):
    obj = get_object_or_404(ListEntry, pk=id)
    context = {}
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/todo")
    return render(request, "todo/delete.html", context)

def todo_create(request):
    context = {}
    if request.method =="POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            obj = ListEntry()
            obj.Description = form['Description'].value()
            obj.isDone = 0
            obj.save()
        return HttpResponseRedirect("/todo")
    else:
        form = CreateForm()
    return render(request, "todo/create.html", {"form": form})

def todo_edit(request, id):
    obj = get_object_or_404(ListEntry, pk=id)
    if request.method =="POST":
        form = EditForm(request.POST)
        if form.is_valid():
            obj.Description = form['Description'].value()
            obj.isDone = form['isDone'].value()
            obj.save()
        return HttpResponseRedirect("/todo")
    else:
        form = EditForm(instance=obj)
    return render(request, "todo/edit.html", {"form": form})
