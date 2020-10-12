from django.db import models


# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'regions'

    def __str__(self):
        return self.name
