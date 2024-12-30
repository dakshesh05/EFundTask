from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # OneToOneField
    bio = models.TextField()

    def __str__(self):
        return self.user.username

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)  # ForeignKey
    name = models.CharField(max_length=100)
    skills = models.ManyToManyField('Skill')  # ManyToManyField

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
