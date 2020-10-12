from django.db import models

from countries.models import Country

# Create your models here.
class University(models.Model):
    id = models.AutoField(db_column='ID',
                          primary_key=True,
                          editable=False)  # Field name made lowercase. This field type is a guess.
    name = models.CharField(db_column='NAME',
                            max_length=200)  # Field name made lowercase.
    active = models.CharField(db_column='ACTIVE', max_length=1)
    country = models.ForeignKey(Country, db_column='COUNTRY_ID', on_delete=models.CASCADE)
    insert_date = models.DateTimeField(db_column='INSERT_DATE', blank=True,
                                       null=True,
                                       editable=False)  # Field name made lowercase.

    class Meta:
        db_table = 'UNIVERSITIES'
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"
