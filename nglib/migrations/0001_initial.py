# Generated by Django 3.2 on 2022-08-05 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=30)),
                ('author_id', models.CharField(max_length=10)),
                ('frequency', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]