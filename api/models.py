from django.db import models

# Create your models here.
class entry(models.Model):
    received_data= models.CharField(max_length=256)

    def __str__(self):
        return self.received_data


