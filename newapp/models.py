from django.db import models

# Create your models here.


class newmodel(models.Model):

 	name = models.CharField(max_length=100)

 	

 	tech = models.CharField(max_length=100,default='')

 	Resume= models.FileField(upload_to='docs/')


 	def __str__(self):

 		return self.name


