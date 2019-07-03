from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationsSerializer, NotificationSerializer
from users.models import User
from categories.models import Category


class NotificationListView(APIView):
    def get(self, request):
        notifications = Notification.objects.all()
        data = NotificationsSerializer(notifications, many=True).data
        return Response(data)

    def post(self, request):
        print(request.data)
        user = User.objects.get(pk=request.data["user"])
        module = Category.objects.get(pk=request.data["module"])
        notification = Notification(user=user, category=module,
                                    title=request.data["title"],
                                    color=request.data["priority"],
                                    summary=request.data["summary"],
                                    content=request.data["content"]

                                    )
        notification.save()
        return Response({"message": "Created post successfully"})


class NotificationDetailView(RetrieveAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
