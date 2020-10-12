from django.urls import path
from .views import UniversityListView

app_name = 'universities'
urlpatterns = [path('', UniversityListView.as_view(), name='list'),
               ]
