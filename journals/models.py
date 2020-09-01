from django.db import models


# Create your models here.
class Journal(models.Model):
    name = models.CharField(max_length=80)

    class Meta:
        db_table = 'journals'
        ordering = ['name']

    def __str__(self):
        return self.name
