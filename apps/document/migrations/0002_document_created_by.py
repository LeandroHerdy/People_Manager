# Generated by Django 3.2.4 on 2021-06-16 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20210616_0952'),
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='employee.employee'),
            preserve_default=False,
        ),
    ]
