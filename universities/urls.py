from django.urls import path
from .views import university_view

app_name = 'universities'
urlpatterns = [path('', university_view, name='list'),
               ]
