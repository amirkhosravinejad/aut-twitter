from django.db import models

# Create your models here.
class login_table(models.Model):
    username = models.CharField(max_length=120)
   # completed = models.BooleanField(default=False)
