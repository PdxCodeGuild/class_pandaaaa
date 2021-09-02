from django.urls import path

from .views import ListStudent, DetailStudent, StudentViewSet, StudentSearch
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', StudentViewSet, basename='students')
urlpatterns = router.urls


# urlpatterns = [
# path('', ListStudent.as_view()),
# path('<int:pk>/', DetailStudent.as_view()),
# ]

urlpatterns.append(
    path('search/custom/', StudentSearch.as_view(), name='studentsearch'))
