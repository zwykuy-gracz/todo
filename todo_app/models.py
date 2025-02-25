from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class TaskStatus(models.Model):
    STATUS_CHOICES = [
        ("NotStarted", "Not Started"),
        ("InProgress", "In Progress"),
        ("AlmostDone", "Almost Done"),
        ("Done", "Done"),
    ]
    task_status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="NotStarted"
    )

    def __str__(self) -> str:
        return self.task_status


class TimeHorizon(models.Model):
    DURATION_CHOICES = [
        ("Short", "Short-term"),
        ("Mid", "Mid-term"),
        ("Long", "Long-term"),
    ]
    duration = models.CharField(
        max_length=10, choices=DURATION_CHOICES, default="Short"
    )

    def __str__(self) -> str:
        return self.duration


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=60, blank=False, unique=True)
    comment = models.TextField(blank=True)
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE)
    duration_lvl = models.ForeignKey(TimeHorizon, on_delete=models.CASCADE)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["deadline"]

    def __str__(self) -> str:
        return self.task


class Counter(models.Model):
    number_of_visitations = models.IntegerField(default=0)

    def __str__(self):
        return str(self.number_of_visitations)
