# Generated by Django 4.2.6 on 2023-10-16 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='doc_name',
            new_name='doct_name',
        ),
    ]