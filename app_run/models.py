from django.contrib.auth.models import User
from django.db import models


class RunStatusEnum(models.TextChoices):
    INIT = 'init', 'Init'
    IN_PROGRESS = 'in_progress', 'In Progress'
    FINISHED = 'finished', 'Finished'


class Run(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    athlete = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=RunStatusEnum.choices,
        default=RunStatusEnum.INIT,
    )
