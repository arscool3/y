from django.db import models


class Child(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Task(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    answer = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    points = models.IntegerField()
    date = models.DateField()
    is_done = models.BooleanField(default=False)
    child = models.ForeignKey(Child, related_name='tasks', on_delete=models.DO_NOTHING)
