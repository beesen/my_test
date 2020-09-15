from django.urls import path
from .views import WebpageDetailView

app_name = 'webpages'
urlpatterns = [
    path('show/<int:pk>/', WebpageDetailView.as_view(), name='show'),
]