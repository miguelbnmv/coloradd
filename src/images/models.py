from django.db import models

# Create your models here.
class Image(models.Model):
	upload = models.ImageField(upload_to='img_uploads')
	likes = models.IntegerField()
