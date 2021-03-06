# Generated by Django 3.1.1 on 2020-09-14 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JournalYear',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('year', models.IntegerField(blank=True, db_column='YEAR', null=True)),
                ('active', models.TextField(blank=True, db_column='ACTIVE', null=True)),
                ('insert_date', models.DateTimeField(blank=True, db_column='INSERT_DATE', null=True)),
            ],
            options={
                'db_table': 'JOURNAL_YEARS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JournalYearIndicator',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('weight', models.TextField(blank=True, db_column='WEIGHT', null=True)),
                ('insert_date', models.DateTimeField(blank=True, db_column='INSERT_DATE', null=True)),
            ],
            options={
                'db_table': 'JOURNAL_YEAR_INDICATORS',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='journal',
            name='id',
            field=models.IntegerField(db_column='ID', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='journal',
            name='name',
            field=models.CharField(db_column='NAME', max_length=80),
        ),
        migrations.AlterModelTable(
            name='journal',
            table='JOURNALS',
        ),
    ]
