# Generated by Django 3.2.6 on 2021-08-29 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('long_description', models.TextField(null=True)),
                ('short_description', models.TextField(null=True)),
                ('fees', models.FloatField(null=True)),
                ('student_number', models.IntegerField(null=True)),
                ('min_age', models.IntegerField(null=True)),
                ('max_age', models.IntegerField(null=True)),
                ('cover_image', models.ImageField(null=True, upload_to=None)),
                ('list_image', models.ImageField(null=True, upload_to=None)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(null=True)),
                ('date_of_event', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('long_description', models.TextField(null=True)),
                ('short_description', models.TextField(null=True)),
                ('price', models.FloatField(null=True)),
                ('min_age', models.IntegerField(null=True)),
                ('max_age', models.IntegerField(null=True)),
                ('cover_image', models.ImageField(null=True, upload_to=None)),
                ('list_image', models.ImageField(null=True, upload_to=None)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(null=True)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to=None)),
                ('category', models.CharField(choices=[('class room', 'class room'), ('competitions', 'competitions')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=14, null=True)),
                ('mail', models.EmailField(max_length=254, null=True)),
                ('specialization', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('quotes', models.TextField(null=True)),
                ('facebook', models.CharField(max_length=50, null=True)),
                ('twitter', models.CharField(max_length=50, null=True)),
                ('google', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registeration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=14, null=True)),
                ('secondary_phone_number', models.CharField(blank=True, max_length=14, null=True)),
                ('mail', models.EmailField(max_length=500, null=True)),
                ('status', models.CharField(choices=[('approved', 'approved'), ('pending', 'pending'), ('denied', 'denied')], default='pending', max_length=50)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='willyWeb.courses')),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='willyWeb.teachers'),
        ),
    ]
