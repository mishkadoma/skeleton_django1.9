from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField()
    body = models.textField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
