# Generated by Django 4.1 on 2022-11-04 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('branch_name', models.CharField(max_length=30)),
                ('branch_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]