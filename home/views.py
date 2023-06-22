from django.shortcuts import render,HttpResponse
from home.models import Task

# Create your views here.
def home(request):
    context={'success':False,'name':'neha'}
    if request.method=="POST":
        #handle tghe form
        title=request.POST['title']
        desc=request.POST['desc']
        print(title,desc)
        ins=Task(taskTitle=title,taskDesc=desc) #to save the table
        ins.save()
        context={'success':True}
    return render(request,'index.html',context)
    
def task(request):
    allTasks=Task.objects.all()
    # print(allTasks)
    # for item in allTasks:# changs made
    #     print(item.taskTitle)
    context={'tasks': allTasks}
    return render(request,'task.html',context)