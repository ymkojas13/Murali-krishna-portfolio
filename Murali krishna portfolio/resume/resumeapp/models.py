from django.db import models

# Create your models here.
class mode(models.Model):
    name = models.CharField(max_length=70)
    subject = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    message = models.TextField(null=True)
