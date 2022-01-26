from django.contrib import admin
from django.urls import path

from blog.views import TodoListApiView, ToDoCreateApiView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoget/',TodoListApiView.as_view(),name='ToDo-get'),
    path('todo/',ToDoCreateApiView.as_view(),name='ToDo-post'),
    path('token/',obtain_auth_token),
]
