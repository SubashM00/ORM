# Ex02 Django ORM Web Application
## Date:14.10.23
## AIM
To develop a Django application to store and retrieve data from a Football Players database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

Include your ER diagram here

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create 10 Football players

## PROGRAM
```
admin.py

from django.contrib import admin
from.models import foodball_player,foodball_playerAdmin
admin.site.register(foodball_player,foodball_playerAdmin)

models.py

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
```

## OUTPUT
![Alt text](<Screenshot (12).png>)


# RESULT
Thus the program for creating a database using ORM hass been executed successfully
