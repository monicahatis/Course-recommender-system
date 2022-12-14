# Generated by Django 4.1.1 on 2022-10-12 13:17

import courses.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('raisec', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertUserLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(upload_to=courses.models.upload_image_path)),
                ('ig_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ClusterClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=255)),
                ('course_title', models.CharField(max_length=255)),
                ('course_image', models.ImageField(upload_to=courses.models.upload_image_path)),
                ('short_description', models.CharField(blank=True, max_length=255, null=True)),
                ('course_description', models.TextField()),
                ('ratting_percentage', models.PositiveBigIntegerField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=True)),
                ('is_instructor', models.BooleanField(default=False)),
                ('cluster_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.clusterclasses')),
            ],
        ),
        migrations.CreateModel(
            name='MinimumRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=3)),
                ('mimimum_point', models.PositiveBigIntegerField(default=0)),
                ('maximum_point', models.PositiveBigIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserMinimumRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimum_requirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.minimumrequirement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourseRattingAndComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratings', models.PositiveBigIntegerField()),
                ('comment', models.CharField(max_length=255)),
                ('created_at', models.DateField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', courses.models.AutoDateTimeField(default=django.utils.timezone.now, editable=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='miniumu_requirement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.minimumrequirement'),
        ),
        migrations.AddField(
            model_name='course',
            name='raisec_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='raisec.raisecgroup'),
        ),
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
