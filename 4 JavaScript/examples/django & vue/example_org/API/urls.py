from django.urls import path
from .views import StudentViewSet
from rest_framework.routers import DefaultRouter

# from .views import ListStudent, DetailStudent

# urlpatterns = [
#     path('', ListStudent.as_view()),
#     path('<int:pk>/', DetailStudent.as_view()),
# ]

# updated to use DRF router
router = DefaultRouter()
router.register('', StudentViewSet, basename='students')
urlpatterns = router.urls