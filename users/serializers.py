from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'username', 'profile_pic', 'first_name',
                  'last_name',
                  'bio',
                  'course',
                  'occupation',
                  'year',
                  'reg_no'
                  )