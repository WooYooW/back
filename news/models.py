from django.db import models
from accounts.models import User

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    press_name = models.CharField(max_length=20)
    original_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

class NewsComment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)