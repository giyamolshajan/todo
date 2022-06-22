from django.shortcuts import render,redirect
from core.form import ToDoForm
from core.models import todolist

# Create your views here.
def home(request):
    # return render(request,'home.html')
    obj_form=ToDoForm()
    todos=todolist.objects.all()
    if request.method=='POST':
        obj_form=ToDoForm(request.POST)
        if obj_form.is_valid():
            obj_form.save()
    return render(request,'home.html',{'form':obj_form,'display':todos})
def update(request,todo_id):
    todo=todolist.objects.get(id=todo_id)
    form=ToDoForm(instance=todo)
    if request.method=='POST':
        obj_form=ToDoForm(request.POST,instance=todo)
        if obj_form.is_valid():
            obj_form.save()
            return redirect('/')
    return render(request,'update.html',{'form':form})
def delete(request,todo_id):
    todo=todolist.objects.get(id=todo_id)
    todo.delete()
    return redirect('home')