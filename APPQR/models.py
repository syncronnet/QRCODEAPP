from django.db import models

class QRCode(models.Model):
    link = models.URLField(max_length=200)

# Create your models here.
