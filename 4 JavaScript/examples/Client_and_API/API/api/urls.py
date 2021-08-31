from django.urls import path
from .views import BoleteAPIView, BoleteDetail, AddBolete

urlpatterns = [
path('', BoleteAPIView.as_view()),
path('<int:pk>/', BoleteDetail.as_view()),
path('add', AddBolete.as_view() )
]