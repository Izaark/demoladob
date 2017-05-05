from rest_framework import serializers
from .models import TodoList, Task

class TaskSerializers(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = ['id','text', 'done', 'created','update']

class TodoListSerializers(serializers.ModelSerializer):

	tasks = TaskSerializers(many = True, read_only=True)
	class Meta:
		model = TodoList
		fields = ['id', 'name', 'created', 'update', 'tasks']