# Generated by Django 3.2.6 on 2022-01-25 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aut_twitter', '0002_auto_20211210_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
            ],
        ),
        migrations.DeleteModel(
            name='api',
        ),
    ]