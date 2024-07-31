from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.contrib.auth import login,authenticate

from django.contrib.auth.decorators import login_required

from .models import Task

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page
            return redirect('dashboard')
        else:
            # Return an invalid login message or render the login page again with an error message
            return render(request, 'loginsignup/login.html', {'error': 'Invalid email or password'})
    else:
        # Render the login form
        return render(request, 'loginsignup/login.html')





def tasks(request):
    tasks=Task.objects.all()
    return render(request,'tasks.html',{'tasks':tasks})


def taskadd(request):
    if request.method=='POST':
        title=request.POST.get('title')
        task=Task.objects.create(title=title)
        task.save()
        return redirect('tasks')
    return render(request,'taskadd.html')

def taskdtl(request,pk):
    task=get_object_or_404(Task,id=pk)
    # task=Task.objects.filter(id=pk)
    return render(request,'taskdtl.html',{'task':task})

def taskdel(request,pk):
    task=get_object_or_404(Task,id=pk)
    task.delete()
    return redirect('tasks')

def taskmod(request,pk):
    task=get_object_or_404(Task,id=pk)
    if task.complete==False:
        task.complete=True
        task.save()
        return redirect('taskdtl',pk)
    else:
        task.complete=False
        task.save()
        return redirect('taskdtl',pk)
