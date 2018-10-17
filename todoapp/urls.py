from django.conf.urls import include, url
from django.urls import path
from . import views
from todoapp.api import ResourceShowTask, ResourceDueDateToday, ResourceDueDateThisweek, ResourceDueDateNextweek, ResourceDueDateOverdue

todoList_Resource1 = ResourceShowTask() 
todoList_Resource2 = ResourceDueDateToday()
todoList_Resource3 = ResourceDueDateThisweek()
todoList_Resource4 = ResourceDueDateNextweek()
todoList_Resource5 = ResourceDueDateOverdue()

urlpatterns = [
    path('', views.firstPage, name='firstPage'),
    path('addTask', views.addTask, name='addTask'),
    path('showTask', views.showTask, name='showTask'),
    path('searchTask', views.searchTask, name='searchTask'),
    path('upcomingDueDates', views.upcomingDueDates, name='upcomingDueDates'),
    path('makeUpdates', views.makeUpdates, name='makeUpdates'),
    path('showTask/api/', include(todoList_Resource1.urls)),
    path('upcomingDueDates/api/', include(todoList_Resource2.urls)),
    path('upcomingDueDates/api/', include(todoList_Resource3.urls)),
    path('upcomingDueDates/api/', include(todoList_Resource4.urls)),
    path('upcomingDueDates/api/', include(todoList_Resource5.urls)),  
]