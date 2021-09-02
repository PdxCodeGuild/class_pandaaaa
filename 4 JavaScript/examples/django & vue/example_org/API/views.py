from rest_framework import generics

from student_list import models
from .serializers import StudentSerializer
from rest_framework import viewsets

# class ListStudent(generics.ListCreateAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = StudentSerializer

# class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Student.objects.all()
#     serializer_class = StudentSerializer

# viewset handles work of both of above
class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer