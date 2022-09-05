# Generated by Django 4.0.4 on 2022-09-05 16:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0008_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.TextField(default=uuid.UUID('7026581c-13fb-4ca4-ab28-fb4430551fb0'), unique=True),
        ),
    ]