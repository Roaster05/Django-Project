# Generated by Django 4.1.3 on 2022-11-15 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Auth_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('club_id', models.IntegerField(primary_key=True, serialize=False)),
                ('club_name', models.CharField(max_length=100)),
                ('club_adminId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth_App.student')),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('venue_Id', models.IntegerField(primary_key=True, serialize=False)),
                ('venue_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SelfActivtiy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('act', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField()),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth_App.student')),
            ],
        ),
        migrations.CreateModel(
            name='ProPic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propic', models.ImageField(default='', upload_to='propic/images')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth_App.student')),
            ],
        ),
        migrations.CreateModel(
            name='Club_Student_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ActivityManager.club')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth_App.student')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('act', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField()),
                ('Club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ActivityManager.club')),
                ('Venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ActivityManager.venue')),
            ],
        ),
    ]
