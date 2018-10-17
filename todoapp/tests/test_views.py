from mixer.backend.django import mixer
from django.urls import reverse
from datetime import datetime
from django.test import RequestFactory
from todoapp.views import addTask, showTask, searchTask, upcomingDueDates, BackgroudTasks, Alerting, HardDeleteTasks
import pytest

@pytest.mark.django_db
class TestViews:

    #   If all variables are correctly defined then it should display status code 200
    def test_addTask(self):
        path = reverse('addTask')
        request = RequestFactory().get(path)
        mixer.blend('todoapp.todoList')
        response = addTask(request)
        assert response.status_code == 200

    #   When the request is made to display the page to show all tasks the status code should be 200
    def test_showTask(self):
        path = reverse('showTask')
        request = RequestFactory().get(path)
        response = showTask(request)
        assert response.status_code == 200

    def test_searchTask(self):
        path = reverse('searchTask')
        request = RequestFactory().get(path)
        response = showTask(request)
        assert response.status_code == 200

    def test_upcomingDueDates(self):
        path = reverse('upcomingDueDates')
        request = RequestFactory().get(path)
        response = showTask(request)
        assert response.status_code == 200
