from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    link = models.TextField(blank=True)
    image = models.ImageField(upload_to='uploads/', blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(null=True, blank=True, max_length=50)
    level = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Experience(models.Model):
    company = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.company
