from django.db import models

# Create your models here.
class api(models.Model):
    username = models.CharField(max_length=120)
    password = models.TextField()
   # completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title