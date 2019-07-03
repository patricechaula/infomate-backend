from django.urls import path

from .views import *

urlpatterns =[
    path('', AssignmentsListView.as_view()),
    path('<pk>', AssignmentDetailView.as_view()),
]