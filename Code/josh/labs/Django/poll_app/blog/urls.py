from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create/', views.create_view, name="post_create"),
    path('<id>', views.detail_view,  name="post_details"),
    path('<id>/update', views.update_view,  name="post_update"),
    path('<id>/delete', views.delete_view, name="post_delete")
]