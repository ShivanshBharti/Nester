from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.views import LoginView
from .forms import *
from django.urls import reverse_lazy

def index(request):
    tasks=Task.objects.all()
    form = Taskform
    if request.method=='POST':
        form=Taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'tasks':tasks,'form':form}
    return render(request,'list.html',context)

def updateTask(request,pk):
    task= Task.objects.get(id=pk)
    form= Taskform(instance=task)
    if request.method=='POST':
        form=Taskform(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}

    return render(request,'update.html',context)

def deleteTask(request,pk):
    item= Task.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect("/")

    context={'item':item}
    return render(request,'delete.html',context)

class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('List')