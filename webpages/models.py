from django.db import models
from tinymce import HTMLField

from organizations.models import Organization


# Create your models here.
class Webpage(models.Model):
    organization = models.ForeignKey(Organization, db_column='ORGANIZATION_ID',
                                     on_delete=models.CASCADE)  # Field name made lowercase. This field type is a guess.
    pageid = models.CharField(db_column='PAGEID', blank=True, null=True,
                              max_length=30)  # Field name made lowercase.
    # pagetext = models.TextField(db_column='PAGETEXT', blank=True, null=True, max_length=4000)  # Field name made lowercase.
    pagetext = HTMLField(db_column='PAGETEXT', blank=True, null=True,
                         max_length=4000)  # Field name made lowercase.
    insert_date = models.DateTimeField(db_column='INSERT_DATE', blank=True, null=True,
                                       editable=False)  # Field name made lowercase.

    class Meta:
        db_table = 'WEBPAGES'
