from django.shortcuts import render

# Create your views here.
# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from .models import Category
from .serialzers import CategorySerializer
from rest_framework.response import Response
from rest_framework import authentication, permissions
from users.models import User

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        data = CategorySerializer(categories, many=True).data
        return  Response(data)

    def post(self, request):
        print(request.data)
        user = User.objects.get(pk=request.data["started_by"])
        category = Category(name = request.data["name"],
                            description=request.data["description"],
                            started_by=user)
        category.save()
        return Response({"message": "Sucessful added module"})


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreate(APIView):

    def get(self, request, format=None):
        """
        Return a list of all users
        :param request:
        :param format:
        :return:
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
