# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Assignment
from .serializers import AssignmentsSerializer, AssignmentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from categories.models import Category
from datetime import datetime
from django.db import models


# helper function

def handle_uploaded_file(f, filename):
    fname = filename + '.pdf'
    with open('c:/tmp/' + fname, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return fname


class AssignmentsListView(APIView):
    def get(self, request):
        assignments = Assignment.objects.all()
        data = AssignmentsSerializer(assignments, many=True).data
        return Response(data)

    def post(self, request):
        print(request.data)
        print(request.FILES)
        user = User.objects.get(pk=request.data['userid'])
        module = Category.objects.get(pk=request.data["category"])
        due_date = models.DateField(request.data['date'])
        handle_uploaded_file(request.FILES['attachment'], request.data['title'])
        assignment = Assignment(
            user=user,
            category=module,
            title=request.data['title'],
            due_date=request.data['date'],
            notes=request.data['notes'],
            file_name=handle_uploaded_file(request.FILES['attachment'], request.data['title']),

        )

        assignment.save()

        return Response({"message": "Created post successfully"})


class AssignmentDetailView(RetrieveAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
