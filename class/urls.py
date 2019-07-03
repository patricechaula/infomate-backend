from django.urls import path

from .views import *

urlpatterns =[
    path('', NotificationListView.as_view()),
    path('<pk>', NotificationDetailView.as_view()),
]