from django.urls import path

from . import views

urlpatterns = [
    path('details/<int:id>', views.details, name = 'details'),
    path('add/', views.add_post, name = 'add'),
    path('remove/<int:id>', views.remove_post, name = 'remove'),
    path('update/<int:id>', views.update, name = 'update'),
    path('all', views.all_posts, name='all'),
    path('search', views.search_posts, name='search')

]