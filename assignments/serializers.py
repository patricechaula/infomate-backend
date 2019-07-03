from rest_framework import serializers
from .models import Assignment
from users.models import User
from categories.models import Category
from categories.serialzers import CategorySerializer


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'username', )


class AssignmentsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model = Assignment
        fields = ('title', 'pub_date','file_link', 'notes','category', 'pk', 'user')

class AssignmentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Assignment
        fields = ('title', 'pub_date','file_link', 'notes','category' ,'color', 'pk', 'user')
