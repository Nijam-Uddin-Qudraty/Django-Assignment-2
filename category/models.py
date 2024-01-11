from django.db import models
# from task.models import TaskModel

# Create your models here.


class TaskCategory(models.Model):
    name = models.CharField(max_length=50)
    # taskmodel = models.ManyToManyField(TaskModel)
    def __str__(self) -> str:
        return f"{self.name}"