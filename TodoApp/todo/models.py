from django.db import models
from datetime import datetime

# Create your models here.
class Todo(models.Model):
    todo_subject = models.CharField(max_length=300, help_text="This Field is required", null=False)
    todo_details = models.TextField()
    todo_date = models.DateTimeField(default=datetime.now, blank=True)
    check = models.BooleanField(default=False)
