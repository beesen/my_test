from django.urls import path
from .views import ranking_view

app_name = 'ranking'
urlpatterns = [path('', ranking_view, name='list'),
               ]
