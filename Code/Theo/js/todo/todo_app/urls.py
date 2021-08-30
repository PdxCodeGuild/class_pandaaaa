"""todo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from .views import TaskList,TaskCreate,TaskUpdate,JSONdata

urlpatterns = [
    path('', TaskList.as_view(),name='index'),
    path('get',JSONdata.as_view(),name='get'),
    path('add/',TaskCreate.as_view(),name='new_task'),
    path('update/<slug:pk>/',TaskUpdate.as_view(),name='update'),
    # path('edit.html', views.new_task, name='new_task'),
    # path('delete_task/<int:pk>', views.delete_task, name='delete_task'),
    # path('todoitem_confirm_delete.html',DeleteTask.as_view(),name='delete_task'),
]
