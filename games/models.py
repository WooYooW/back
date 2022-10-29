from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from accounts.models import User
# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=20)


class Gamerecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    playtime = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    answer_count = models.IntegerField(default=0)
    moves_count = models.IntegerField(default=0)