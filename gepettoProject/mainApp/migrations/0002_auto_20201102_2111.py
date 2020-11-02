# Generated by Django 3.1.3 on 2020-11-02 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_probability',
            field=models.CharField(default='0', max_length=80),
        ),
    ]
