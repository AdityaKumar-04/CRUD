# Generated by Django 4.2.1 on 2023-10-07 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='img',
            field=models.ImageField(null=True, upload_to='media'),
        ),
    ]
