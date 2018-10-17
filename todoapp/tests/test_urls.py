from django.urls import reverse, resolve

class TestUrls:

    def test_urls(self):
        path = reverse('addTask')
        assert resolve(path).view_name == 'addTask'

        path = reverse('showTask')
        assert resolve(path).view_name == 'showTask'

        path = reverse('searchTask')
        assert resolve(path).view_name == 'searchTask'

        path = reverse('upcomingDueDates')
        assert resolve(path).view_name == 'upcomingDueDates'

        path = reverse('makeUpdates')
        assert resolve(path).view_name == 'makeUpdates'