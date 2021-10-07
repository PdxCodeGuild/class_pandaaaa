from django.shortcuts import render
from rest_framework import generics

from studentsapp import models
from .serializers import StudentSerializer

class ListStudent(generics.ListCreateAPIView):
    queryset = models.Students.objects.all()
    serializer_class = StudentSerializer


class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Students.objects.all()
    serializer_class = StudentSerializer