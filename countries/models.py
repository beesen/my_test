from django.db import models

from regions.models import Region

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso_code_2 = models.CharField(db_column='COUNTRY_ISO_CODE_2', max_length=2)

    class Meta:
        db_table = 'COUNTRIES'

    def __str__(self):
        return f"{self.name}"

