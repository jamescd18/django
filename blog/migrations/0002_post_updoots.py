# Generated by Django 3.0 on 2019-12-31 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updoots',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
