# Generated by Django 3.0.4 on 2020-03-30 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accountApp', '0011_auto_20200330_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sidebar',
            name='user',
        ),
        migrations.AddField(
            model_name='sidebar',
            name='student',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='accountApp.Profile'),
            preserve_default=False,
        ),
    ]
