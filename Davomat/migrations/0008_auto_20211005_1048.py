# Generated by Django 3.2.7 on 2021-10-05 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Davomat', '0007_auto_20211005_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='davomats',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='name',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
