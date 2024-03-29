# Generated by Django 3.2.9 on 2021-12-05 21:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseRegisteration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=14, null=True)),
                ('secondary_phone_number', models.CharField(blank=True, max_length=14, null=True)),
                ('mail', models.EmailField(max_length=500, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('status', models.CharField(choices=[('approved', 'approved'), ('pending', 'pending'), ('denied', 'denied')], default='pending', max_length=50)),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.course')),
            ],
            options={
                'verbose_name_plural': 'Registerations',
            },
        ),
        migrations.CreateModel(
            name='CompetitionRegisteration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=14, null=True)),
                ('secondary_phone_number', models.CharField(blank=True, max_length=14, null=True)),
                ('mail', models.EmailField(max_length=500, null=True)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('status', models.CharField(choices=[('approved', 'approved'), ('pending', 'pending'), ('denied', 'denied')], default='pending', max_length=50)),
                ('competition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.competition')),
            ],
            options={
                'verbose_name_plural': 'Registeration Competition',
            },
        ),
    ]
