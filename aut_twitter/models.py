from django.db import models

# Create your models here.
<<<<<<< HEAD
class login_table(models.Model):
    username = models.CharField(max_length=120)
   # completed = models.BooleanField(default=False)
=======
class api(models.Model):
    username = models.CharField(max_length=120)
    password = models.TextField()
   # completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
>>>>>>> b28e892e132bbf547a3bf56658d604d1bd197493
