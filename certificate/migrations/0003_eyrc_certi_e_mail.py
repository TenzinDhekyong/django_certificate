# Generated by Django 2.0.7 on 2020-05-04 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0002_remove_eyrc_certi_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='eyrc_certi',
            name='e_mail',
            field=models.EmailField(default='SOME STRING', max_length=254),
        ),
    ]
