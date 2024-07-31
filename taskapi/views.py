from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from task.models import Task,TaskSerializers


from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response



@api_view(['GET','POST'])
def tasks(request):
    if request.method=='GET':
        tasks=Task.objects.all()
        serializer=TaskSerializers(tasks,many=True)
        return JsonResponse({'tasks':serializer.data})
    elif request.method=='POST':
        json=JSONParser().parse(request) 
        serializer=TaskSerializers(data=json)
        if serializer.is_valid(): 
            serializer.save()
            return JsonResponse({'Task':serializer.data})
        else :
            return JsonResponse({'message':serializer.errors})


@api_view(['GET','DELETE','PUT'])
def taskdtl(request,pk):
    try:
        task=Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=404)
    
    if request.method =='GET':
        serializer=TaskSerializers(task)
        return JsonResponse(serializer.data)
    
    if request.method =='DELETE':
        task.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
    
    if request.method =='PUT':
        json=JSONParser().parse(request)
        serializer=TaskSerializers(task,data=json)
        if serializer.is_valid(): 
            serializer.save()
            return Response({'Task':serializer.data})
        else :
            return Response({'message':serializer.errors})














def taskadd(request):
    if request.method=='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        task=Task.objects.create(title=title,description=description)
        task.save()
        return redirect('tasks')
    return render(request,'taskadd.html')



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