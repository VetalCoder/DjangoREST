from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=450)
    year = models.IntegerField()

    def __str__(self):
        return f"Name: {self.title}, desc: {self.desc}, year: {self.year}."