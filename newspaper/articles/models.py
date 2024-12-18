from django.db import models
from django.conf import settings
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, #only for models.py, anywhere else it's get_user_model()
        on_delete = models.CASCADE
    )
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
    
class Comment(models.Model):
    Article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=150)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse("article_list")
    