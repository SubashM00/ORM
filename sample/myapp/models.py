from django.db import models
from django.contrib import admin 
class foodball_player(models.Model):
    p_name=models.CharField(max_length=20)
    p_age=models.IntegerField()
    p_country=models.CharField(max_length=20)
    p_email=models.EmailField()
    p_dob=models.DateField()
class foodball_playerAdmin(admin.ModelAdmin):
    list_display=('p_name','p_age','p_country','p_email','p_dob')