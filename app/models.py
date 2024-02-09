from django.db import models

# Crea te your models here.
class Heros(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()

    def __str__(self):
        return self.name
        

class Movies(models.Model):
    name=models.ForeignKey(Heros,on_delete=models.CASCADE,related_name='hero')
    mname=models.CharField(max_length=100)

    def  __str__(self):
        return self.mname