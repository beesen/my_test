from django.urls import path
from .views import regions_simple_view, regions_selected_view

app_name = 'regions'
urlpatterns = [path('simple/', regions_simple_view, name='simple'),
               path('changed/', regions_selected_view, name='changed'),
               ]
