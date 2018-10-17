from django.shortcuts import render, redirect
from .models import todoList
from django.db.models import Q
from django.utils.dateparse import parse_date
from django.utils.dateformat import format
from datetime import datetime, timedelta, date, time
import uuid, pytz

# Create your views here.

def firstPage(request):
    return render(request, 'todoapp/addtask.html')

def addTask(request):
#    todoList.objects.all().delete()
    Id = str(uuid.uuid1())
    Title = request.POST.get('Title', 'None')
    Description = request.POST.get('Description', 'None')
    temp_tasks = request.POST.get('SubTasks', 'None')
    SubTasks = temp_tasks.split(',')
    Status = request.POST.get('Status', 'Pending')
    temp_date = request.POST.get('DueDate', 'None')
    if (temp_date == 'None') or (type(temp_date)) == "str":
        DueDate = datetime.now().date() + timedelta(days=30)
    else:
        DueDate = parse_date(temp_date)
    Alert = request.POST.get('Alert', int(0))
    todoapp = todoList(
        Local_id=Id,
        Title=Title,
        Description=Description,
        SubTasks=SubTasks,
        Status=Status,
        DueDate=DueDate,
        Alert=Alert,
        Symbol="",
        Visibility="yes"
    )
    todoapp.save()
    return render(request, 'todoapp/addtask.html')

def showTask(request):
    BackgroudTasks()
    result = todoList.objects.filter(Visibility="yes").order_by('DueDate')
    context = {
        'posts': result.all() 
    }
    return render(request, 'todoapp/display.html',context)

def searchTask(request):
    BackgroudTasks()
    query = request.POST.get('Search', 'None')
    result = todoList.objects.filter(Q(Title__icontains=query)).filter(Visibility="yes").order_by('DueDate')
    context = {
        'posts': result.all() 
    }
    return render(request, 'todoapp/display.html', context)

def upcomingDueDates(request):
    BackgroudTasks()
    DueDateFilter = request.POST.get('ComingDueDates', 'None')
    if DueDateFilter == "Today":
        todaysDate = datetime.today().strftime('%Y-%m-%d')
        result = todoList.objects.filter(DueDate__contains=todaysDate).filter(Visibility="yes").order_by('DueDate')
        context = {
        'posts': result.all() 
        }
    elif DueDateFilter == "ThisWeek":
        today = datetime.now().date()
        start = today - timedelta(days=today.weekday())
        end = start + timedelta(days=6)
        result = todoList.objects.filter(DueDate__range=(start, end)).filter(Visibility="yes").order_by('DueDate')
        context = {
            'posts': result.all() 
        }
    elif DueDateFilter == "NextWeek":
        today = datetime.now().date()
        start = today - timedelta(days=today.weekday())
        finalStart = start + timedelta(days=7)
        end = finalStart + timedelta(days=6)
        result = todoList.objects.filter(DueDate__range=(finalStart, end)).filter(Visibility="yes").order_by('DueDate')
        context = {
            'posts': result.all() 
        }
    elif DueDateFilter == "Overdue":
        today = datetime.now().date()
        start = today + timedelta(days=-1000) 
        end = today + timedelta(days=-1)
        result = todoList.objects.filter(DueDate__range=(start, end)).filter(Visibility="yes").order_by('DueDate')
        context = {
            'posts': result.all() 
        }
    return render(request, 'todoapp/display.html', context)

def makeUpdates(request):
    updatedStatus1 = request.POST.get('Status1', 'None')
    updatedStatus2 = request.POST.get('Status2', 'None')
    updatedDelete = request.POST.get('DeleteTask', 'None')
    print("Task Id: ")
    print(updatedStatus1)
    tasks = todoList.objects.all()
    for task in tasks:
        if str(task.Local_id) == str(request.POST["taskId"]):
            if updatedDelete != 'None':
                task.Visibility = "no"
                task.HardDeleteDate = datetime.now().date() + timedelta(days=30)
                task.save()
            if str(updatedStatus1) == "Complete":
                task.Status = "Complete"
                task.save()
            if str(updatedStatus2) == "Pending":
                task.Status = "Pending"
                task.save()
            break
    return render(request, 'todoapp/update.html')

def BackgroudTasks():
    HardDeleteTasks()
    Alerting()
    return 0

def HardDeleteTasks():
    tasks = todoList.objects.all()
    now = datetime.now().date()
    for task in tasks:
        if task.Visibility == "null":
            if task.HardDeleteDate != "NoneType":
                if now >= task.HardDeleteDate:
                    task.delete()
                    task.save()
    return 0

def Alerting():
    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(tz)
    now = now.strftime('%Y-%m-%d %H:%M:%S')
    now = datetime.strptime(now, '%Y-%m-%d %H:%M:%S')
    print("now")
    print(type(now))
    print(now)
    tempDueDateTime = datetime.strptime('00:00', '%H:%M').time()
    tasks = todoList.objects.all()
    for task in tasks:
        if task.Status == "Pending":
            dueDateTime = datetime.combine(task.DueDate, tempDueDateTime)
            alertTime = dueDateTime - timedelta(hours=int(task.Alert))
            print("DueDateTime")
            print(type(dueDateTime))
            print(dueDateTime)
            print("alertTime")
            print(type(alertTime))
            print(alertTime)
            if alertTime <= now <= dueDateTime:
                task.Symbol = "yes"
        else:
            task.Symbol = "no"
        task.save()
    return 0