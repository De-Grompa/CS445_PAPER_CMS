from django.db import models

# Create your models here.
class Username(models.Model):
    username_text = models.CharField(max_length=100)
    
class Password(models.Model):
    username = models.ForeignKey(Username, on_delete=models.CASCADE)
