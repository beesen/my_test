from django.urls import path
from .views import JournalListView, journal_detail_view

app_name = 'journals'
urlpatterns = [
    path('', JournalListView.as_view(), name='list'),
    path('detail/', journal_detail_view, name='detail'),
]