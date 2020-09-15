from django.db import models

# Create your models here.
class Webpage(models.Model):
    pageid = models.CharField(db_column='PAGEID', blank=True, null=True, max_length=30)  # Field name made lowercase.
    pagetext = models.CharField(db_column='PAGETEXT', blank=True, null=True, max_length=4000)  # Field name made lowercase.
#    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    insert_date = models.DateTimeField(db_column='INSERT_DATE', blank=True, null=True)  # Field name made lowercase.
    organization_id = models.IntegerField(db_column='ORGANIZATION_ID', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'WEBPAGES'