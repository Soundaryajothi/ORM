
from django.db import models
from django.contrib import admin
class footballplayer(models.Model):
    name=models.CharField(max_length=15)
    player_id=models.CharField(max_length=100)
    weight=models.IntegerField()
    age=models.IntegerField()
    members=models.CharField(max_length=20)
    

class footballplayerAdmin (admin.ModelAdmin):
    list_display=('name','player_id','weight','age','members')
