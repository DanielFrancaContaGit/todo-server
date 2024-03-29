from django.db import models

# Create your models here.

class Todo(models.Model):
    objects=models.Manager
    content = models.CharField(max_length=400)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return f'conteudo do todo: {self.content}'