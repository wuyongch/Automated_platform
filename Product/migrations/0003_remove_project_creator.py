# Generated by Django 2.1.7 on 2019-06-27 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='creator',
        ),
    ]
