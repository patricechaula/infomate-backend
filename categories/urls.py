from django.urls import path

from .views import *

urlpatterns =[
    path('', CategoryListView.as_view()),
    path('<pk>', CategoryDetailView.as_view()),

]