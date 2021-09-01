from django.urls import path
from .views import ListStudent, DetailStudent,CreateStudent

urlpatterns = [
    path('',ListStudent.as_view()),
    path('<int:pk>/',DetailStudent.as_view()),
    path('new/',CreateStudent.as_view()),
]