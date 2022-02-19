from distutils.command.upload import upload
from tokenize import blank_re
from django.db import models

# Create your models here.
class File(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='myapp/images',null=True,blank=True)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="")
