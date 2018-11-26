from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    # slug = models.SlugField(max_length=200,db_index=True,unique=True)
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500)
    create_date = models.DateTimeField(default=timezone.now())
    upload = models.ImageField(upload_to='uploads/%Y/%m/%d/',blank=True)

    # def get_absolute_url(self):
    #     return reverse("home")

    def __str__(self):
        return self.title

