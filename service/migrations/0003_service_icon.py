# Generated by Django 5.0.6 on 2024-07-07 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_service_service_title_alter_service_service_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.FileField(default=None, max_length=250, null=True, upload_to=',media/'),
        ),
    ]