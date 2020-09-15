from django.urls import path
from .views import sandbox_view

app_name = 'sandbox'
urlpatterns = [path('', sandbox_view, name='list'),
               ]
