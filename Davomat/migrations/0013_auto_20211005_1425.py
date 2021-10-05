# Generated by Django 3.2.7 on 2021-10-05 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Davomat', '0012_remove_davomat_group_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Davomats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Davomat.students')),
            ],
        ),
        migrations.DeleteModel(
            name='Davomat',
        ),
    ]
