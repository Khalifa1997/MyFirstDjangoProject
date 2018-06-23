from django.db import models
from datetime import datetime

class board(models.Model):
    name= models.CharField(max_length=255, unique=True)
    description= models.CharField(max_length=500)
    def __str__(self):
        return self.name

class thread(models.Model):
    board= models.ForeignKey(board, on_delete=models.CASCADE)
    title= models.CharField(max_length=255)
    author= models.CharField(max_length=150, default='')
    body= models.TextField()
    date= models.DateField()
    def __str__(self):
        return self.title


class reply(models.Model):
    thread=models.ForeignKey(thread,on_delete=models.CASCADE)
    text=models.TextField()
    date = models.DateTimeField(default=datetime.now)
    created_by=  models.CharField(max_length=150)
    def __str__(self):
        return self.created_by
