from django.urls import path
from . import views

urlpatterns = [
    path('', views.firstPage, name='firstPage'),
    path('addTask', views.addTask, name='addTask'),
    path('showTask', views.showTask, name='showTask'),
    path('searchTask', views.searchTask, name='searchTask'),
    path('upcomingDueDates', views.upcomingDueDates, name='upcomingDueDates'),
    path('makeUpdates', views.makeUpdates, name='makeUpdates'),        
]