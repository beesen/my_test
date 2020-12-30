from django.db import models


# Create your models here.
class Indicator(models.Model):
    id = models.IntegerField(db_column='ID',
                             primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=100)  # Field name made lowercase.
    insert_date = models.DateTimeField(db_column='INSERT_DATE', blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'INDICATORS'
