# Generated by Django 4.0.3 on 2022-03-29 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0002_cartitem_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
