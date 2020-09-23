from django.urls import path
from .views import WebpageDetailView, WebpageListView, WebpageUpdateView, WebpageDeleteView, WebpageCreateView
app_name = 'webpages'
urlpatterns = [
    path('show/<int:pk>/', WebpageDetailView.as_view(), name='show'),
    path('', WebpageListView.as_view(), name='list'),
    path('edit/<int:pk>', WebpageUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', WebpageDeleteView.as_view(), name='delete'),
    path('create/', WebpageCreateView.as_view(), name='create'),
]