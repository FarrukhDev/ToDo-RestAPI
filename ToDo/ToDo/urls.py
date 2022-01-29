from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
from blog.views import TodoListApiView,RetriveApiVIEW #ToDoCreateApiView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="ToDo rest API",
      default_version='v1',
      description="ToDo uchun yozilgan rest api lar to`plami",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="farruxbekergashaliev@gmail.com"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/',TodoListApiView.as_view(),name='ToDo-get'),
    # path('todo/',ToDoCreateApiView.as_view(),name='ToDo-post'),
    path('todoget/<int:pk>',RetriveApiVIEW.as_view(),name='retrive'),
    # path('token/',obtain_auth_token),
    path('get-token',TokenObtainPairView.as_view()),
    path('refresh-token',TokenRefreshView.as_view()),
    #Api ning documintatsiyalari
    path('docs',schema_view.with_ui("swagger",cache_timeout=0)),
    path('redoc',schema_view.with_ui("redoc",cache_timeout=0)),
]
