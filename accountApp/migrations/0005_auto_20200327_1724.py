# Generated by Django 3.0.4 on 2020-03-27 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountApp', '0004_profile_sfedu_schadule'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='sfedu_schadule',
            new_name='schadule',
        ),
        migrations.AddField(
            model_name='profile',
            name='scoreline',
            field=models.CharField(default='empty', max_length=5000),
        ),
        migrations.AddField(
            model_name='profile',
            name='student_name',
            field=models.CharField(default='empty', max_length=5000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sfedu_username',
            field=models.CharField(default='Студент', max_length=500),
        ),
    ]
