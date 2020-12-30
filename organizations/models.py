from django.db import models


# Create your models here.
class Organization(models.Model):
    id = models.AutoField(db_column='ID',
                             primary_key=True, editable=False)  # Field name made lowercase. This field type is a guess.
    name = models.CharField(db_column='NAME', unique=True, max_length=100)  # Field name made lowercase.
    linked_organization_id = models.IntegerField(db_column='LINKED_ORGANIZATION_ID',
                                                 blank=True,
                                                 null=True)  # Field name made lowercase.
    insert_date = models.DateTimeField(db_column='INSERT_DATE', blank=True,
                                       null=True, editable=False)  # Field name made lowercase.

    class Meta:
        db_table = 'ORGANIZATIONS'

    def __str__(self):
        return f"{self.name}"