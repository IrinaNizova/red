from django.db import models

class ImagesParams(models.Model):
    title = models.CharField(max_length=200)
    percent_red = models.FloatField()
    time = models.DateTimeField()

    def __str__(self):
        return self.title

class Subscribers(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=200, blank=True)
    level_red = models.IntegerField()

    def __str__(self):
        return self.email

