# Generated by Django 2.2.10 on 2020-03-22 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0009_remove_collection_collection_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection_has_games',
            name='collection_id',
        ),
        migrations.AddField(
            model_name='collection_has_games',
            name='collection_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
