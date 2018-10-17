import requests
import json

BASE_URL = "http://127.0.0.1:8000/"

def test_showtask():
    response = requests.get(BASE_URL + "showTask/api/showtask/?format=json")
    assert response.status_code == 200
    assert type(response.json()) == dict
    response = requests.get(BASE_URL + "showTask/api/task/?format=json")
    assert response.status_code == 404

def test_DueDateToday():
    response = requests.get(BASE_URL + "upcomingDueDates/api/today/?format=json")
    assert response.status_code == 200
    response = requests.get(BASE_URL + "upcomingDueDates/api/tody/?format=json")
    assert response.status_code == 404

def test_DueDateThisweek():
    response = requests.get(BASE_URL + "upcomingDueDates/api/thisweek/?format=json")
    assert response.status_code == 200
    response = requests.get(BASE_URL + "upcomingDueDates/api/thiswek/?format=json")
    assert response.status_code == 404

def test_DueDateNextweek():
    response = requests.get(BASE_URL + "upcomingDueDates/api/nextweek/?format=json")
    assert response.status_code == 200
    response = requests.get(BASE_URL + "upcomingDueDates/api/nextwak/?format=json")
    assert response.status_code == 404

def test_DueDateOverdue():
    response = requests.get(BASE_URL + "upcomingDueDates/api/overdue/?format=json")
    assert response.status_code == 200
    response = requests.get(BASE_URL + "upcomingDueDates/api/overde/?format=json")
    assert response.status_code == 404