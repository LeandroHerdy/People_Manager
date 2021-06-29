# Generated by Django 3.2.4 on 2021-06-22 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('departament', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='departament',
            name='company',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.PROTECT, to='company.company'),
            preserve_default=False,
        ),
    ]
