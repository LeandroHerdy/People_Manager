# Generated by Django 3.2.4 on 2021-06-22 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0002_document_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='archive',
            field=models.FileField(default=1, upload_to='document'),
            preserve_default=False,
        ),
    ]
