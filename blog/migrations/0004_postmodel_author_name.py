# Generated by Django 2.0.1 on 2018-02-03 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180130_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='author_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
