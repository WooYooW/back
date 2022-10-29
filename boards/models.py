from django.db import models
from accounts.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.

class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True)
    thumbnail = ProcessedImageField(upload_to='images/', blank=True,
                                processors=[ResizeToFill(150, 100)],
                                format='JPEG',
                                options={'quality': 80})
class BoardComment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)