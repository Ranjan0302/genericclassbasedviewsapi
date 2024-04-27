from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics

# Create your views here.
class SnippetList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
