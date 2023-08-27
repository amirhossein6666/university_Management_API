# Generated by Django 4.2.4 on 2023-08-27 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('professor', '0001_initial'),
        ('custom_token', '0001_initial'),
        ('student', '0001_initial'),
        ('myAdmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcustomtoken',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='custom_token', to='student.student'),
        ),
        migrations.AddField(
            model_name='professorcustomtoken',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='custom_token', to='professor.professor'),
        ),
        migrations.AddField(
            model_name='admincustomtoken',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='custom_token', to='myAdmin.myadmin'),
        ),
    ]
