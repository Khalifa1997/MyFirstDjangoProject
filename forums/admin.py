from django.contrib import admin
from .models import thread,reply,board

# Register your models here.
admin.site.register(thread)
admin.site.register(reply)
admin.site.register(board)