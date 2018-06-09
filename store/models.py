from django.db import models

class company(models.Model):
    name=models.CharField(max_length=500)
    est_date=models.DateField()
    location=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class product(models.Model):
    company=models.ForeignKey('company',on_delete=models.CASCADE)
    name=models.CharField(max_length=500)    
    category = models.CharField(max_length=500)
    price= models.FloatField()
    size= models.PositiveIntegerField()
    picture=models.CharField(max_length=2000, default='')
    reviews= models.TextField()
    def __str__(self):
        return self.name