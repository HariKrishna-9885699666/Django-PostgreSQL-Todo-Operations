from django.db import models

class TodoItem(models.Model):
    task = models.CharField(max_length=100)  # Text field for the task description
    completed = models.BooleanField(default=False)  # Boolean field for completion status
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when created

    def __str__(self):
        return self.task