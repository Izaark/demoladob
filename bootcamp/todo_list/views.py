from django.shortcuts import render

#from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from .models import TodoList
from .serializers import TodoListSerializers

class ListViewset(ModelViewSet):

	queryset =  TodoList.objects.all()
	serializer_class = TodoListSerializers