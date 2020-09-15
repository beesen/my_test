from django.db import models


# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'regions'

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso_code_2 = models.CharField(max_length=2)

    class Meta:
        db_table = 'countries'

    def __str__(self):
        return f"{self.name}/{self.iso_code_2}"
