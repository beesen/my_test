from django.urls import path
from .views import JournalListView

app_name = 'journals'
urlpatterns = [path('', JournalListView.as_view(), name='list'),
              ]