from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500)
    create_date = models.DateTimeField(default=timezone.now())

    def get_absolute_url(self):
        return reverse("app:home")

    def __str__(self):
        return self.title

