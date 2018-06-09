from django.contrib import admin
from .models import article, comment

# Register your models here.
admin.site.register(article)
admin.site.register(comment)