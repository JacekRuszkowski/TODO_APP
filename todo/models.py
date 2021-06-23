from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Board(models.Model):
    board_name = models.CharField(max_length=25)
    day = models.DateTimeField(default=timezone.now)
    board_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.board_name


class Task(models.Model):
    task_name = models.CharField(max_length=35)
    done = models.BooleanField(default=False)
    not_done = models.BooleanField(default=False)
    task_board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        upper_first = self.task_name[0].upper() + self.task_name[1:]
        return upper_first
