from rest_framework import generics, viewsets
from rest_framework import filters
from myapp import models
from .serializers import StudentSerializer


class ListStudent(generics.ListCreateAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['firstName', 'lastName']


class StudentSearch(generics.ListAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^firstName', '^lastName']


class DetailStudent(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = StudentSerializer
