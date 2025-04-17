from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Mxl_files(models.Model):
    mxl_file = models.FileField(null=True, validators=[FileExtensionValidator(['mxl', 'musicxml'])], unique=True)


class Tester_table(models.Model):
    message = models.CharField(max_length=300)
    name = models.CharField(max_length=20)


class video_files(models.Model):
    video_files = models.FileField(null=True, validators=[FileExtensionValidator(['mp4'])], unique=True)