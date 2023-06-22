from django.contrib import admin
from home.models import Task

# Register your models here.
admin.site.register(Task)
 #when you are creating a superuser after creating the model,first run python manage.py makemigrations
 #migrate will create the table