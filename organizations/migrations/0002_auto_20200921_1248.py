# Generated by Django 3.1.1 on 2020-09-21 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='id',
            field=models.AutoField(db_column='ID', editable=False, primary_key=True, serialize=False),
        ),
    ]