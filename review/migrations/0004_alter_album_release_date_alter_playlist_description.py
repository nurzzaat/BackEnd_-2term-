# Generated by Django 4.1.7 on 2023-05-13 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_alter_playlist_user_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='description',
            field=models.TextField(),
        ),
    ]
