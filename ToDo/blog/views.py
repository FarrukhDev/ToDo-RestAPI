from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView, CreateAPIView
from blog.serializer import TodoSerializer
from blog.models import Todo
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class TodoListApiView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering_fields = ["title"]
    search_fields = ["title", "description"]
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]
class ToDoCreateApiView(CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
