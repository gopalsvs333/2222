from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer,SubjectSerializer
from .models import Student,Subject

# Create your views here.




class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class=SubjectSerializer
