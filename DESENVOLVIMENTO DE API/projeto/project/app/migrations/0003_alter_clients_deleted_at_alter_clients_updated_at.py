# Generated by Django 5.0.7 on 2024-07-28 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_clients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]