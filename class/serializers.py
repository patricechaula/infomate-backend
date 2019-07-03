from rest_framework import serializers
from .models import Notification
from users.models import User
from categories.models import Category
from categories.serialzers import CategorySerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'username', 'profile_pic')


class NotificationsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model = Notification
        fields = ('title', 'pub_date', 'summary','category','color', 'pk', 'user')

class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Notification
        fields = ('title', 'pub_date', 'content','category' ,'color', 'pk', 'user')
