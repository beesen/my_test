from django.db import models


# Create your models here.
class Organizations(models.Model):
    id = models.IntegerField(db_column='ID',
                             primary_key=True)  # Field name made lowercase. This field type is a guess.
    name = models.CharField(db_column='NAME', max_length=100)  # Field name made lowercase.
    linked_organization_id = models.IntegerField(db_column='LINKED_ORGANIZATION_ID',
                                                 blank=True,
                                                 null=True)  # Field name made lowercase.
    insert_date = models.DateTimeField(db_column='INSERT_DATE', blank=True,
                                       null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'ORGANIZATIONS'
