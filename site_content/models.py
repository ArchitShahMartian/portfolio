from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    last_updated_at = models.DateField()