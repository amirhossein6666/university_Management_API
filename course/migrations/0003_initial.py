# Generated by Django 4.2.4 on 2023-09-10 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0002_initial'),
        ('professor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professor.professor'),
        ),
    ]
