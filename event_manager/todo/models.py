from django.db import models


class Todo(models.Model):

    name = models.CharField(max_length=100)  # Varchar 100
    description = models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name