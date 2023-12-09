from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    subject = models.CharField(max_length=200)
    content = QuillField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    background = models.CharField(max_length=200)

    def __str__(self):
        return self.subject
    
    def get_absolute_url(self):
        return reverse('pestpoge:blog_list')

