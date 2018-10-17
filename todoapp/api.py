from todoapp.models import todoList
from tastypie.resources import ModelResource
from tastypie.constants import ALL
from todoapp.models import todoList
from datetime import datetime, timedelta

class ResourceShowTask(ModelResource):
    class Meta:
        queryset = todoList.objects.all()
        resource_name = "showtask"

class ResourceDueDateToday(ModelResource):
    class Meta:
        todaysDate = datetime.today().strftime('%Y-%m-%d')
        queryset = todoList.objects.filter(DueDate__contains=todaysDate).filter(Visibility="yes").order_by('DueDate')
        resource_name = "today"

class ResourceDueDateThisweek(ModelResource):
    class Meta:
        today = datetime.now().date()
        start = today - timedelta(days=today.weekday())
        end = start + timedelta(days=6)
        queryset = todoList.objects.filter(DueDate__range=(start, end)).filter(Visibility="yes").order_by('DueDate')
        resource_name = "thisweek"

class ResourceDueDateNextweek(ModelResource):
    class Meta:
        today = datetime.now().date()
        start = today - timedelta(days=today.weekday())
        finalStart = start + timedelta(days=7)
        end = finalStart + timedelta(days=6)
        queryset = todoList.objects.filter(DueDate__range=(finalStart, end)).filter(Visibility="yes").order_by('DueDate')
        resource_name = "nextweek"

class ResourceDueDateOverdue(ModelResource):
    class Meta:
        today = datetime.now().date()
        start = today + timedelta(days=-1000) 
        end = today + timedelta(days=-1)
        queryset = todoList.objects.filter(DueDate__range=(start, end)).filter(Visibility="yes").order_by('DueDate')
        resource_name = "overdue"