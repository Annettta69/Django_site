from django.db import models

class Articles(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    post = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
