# Generated by Django 4.1.1 on 2022-10-23 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactfromuser',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.subjects'),
        ),
    ]
