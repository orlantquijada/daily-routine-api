# Generated by Django 3.0.5 on 2020-05-03 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_auto_20200504_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='tasks/icons/'),
        ),
    ]
