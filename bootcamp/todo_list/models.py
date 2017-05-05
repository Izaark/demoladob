from django.db import models
from django.conf import settings

class TodoList(models.Model):

	name = models.CharField(max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "TodoList"
		verbose_name_plural = "TodoLists"

	def __str__(self):
		return self.name 


class Task(models.Model):
	'''
	Task model
	'''
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	todo_list = models.ForeignKey(TodoList, related_name='tasks')
	text = models.CharField(max_length=200)
	done = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = "Task"
		verbose_name_plural = "Tasks"

	def __str__(self):
		return self.text
