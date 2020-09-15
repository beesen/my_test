from django.db import models

from indicators.models import Indicator


# Create your models here.
class Journal(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='NAME', max_length=80)

    class Meta:
        db_table = 'JOURNALS'
        ordering = ['name']


class JournalYear(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    year = models.IntegerField(db_column='YEAR', blank=True, null=True)  # Field name made lowercase.
    journal = models.ForeignKey(Journal, db_column='JOURNAL_ID', on_delete=models.CASCADE)  # Field name made lowercase.
    active = models.TextField(db_column='ACTIVE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    insert_date = models.DateTimeField(db_column='INSERT_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'JOURNAL_YEARS'


class JournalYearIndicator(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    journal_year = models.ForeignKey(JournalYear, db_column='JOURNAL_YEAR_ID', on_delete=models.CASCADE)  # Field name made lowercase.
    indicator = models.ForeignKey(Indicator, db_column='INDICATOR_ID', on_delete=models.CASCADE)  # Field name made lowercase.
    weight = models.TextField(db_column='WEIGHT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    insert_date = models.DateTimeField(db_column='INSERT_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'JOURNAL_YEAR_INDICATORS'