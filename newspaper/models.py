from django.db import models
from datetime import datetime
class article(models.Model):
    title= models.CharField(max_length=150)
    body= models.TextField()
    date= models.DateField()
    author= models.CharField(max_length=150, default='')

    def __str__(self):
        return self.title + ' - ' + str(self.author)
    

class comment(models.Model):
    main_article=models.ForeignKey('article',on_delete=models.CASCADE)
    text=models.TextField(default='Empty reply')
    date = models.DateTimeField(default=datetime.now, blank=True)
    created_by=  models.CharField(max_length=150, default='')
    def __str__(self):
        return self.text
    