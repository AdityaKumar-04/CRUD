from django.db import models

# Create your models here.
class Student(models.Model):

    name= models.CharField(max_length=255)
    age= models.IntegerField()
    city= models.CharField(max_length=255)
    img= models.ImageField(null=True ,upload_to='media/')