# Generated by Django 3.2.5 on 2021-07-27 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wansentialsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80)),
                ('picture', models.ImageField(default='default.png', upload_to='images/')),
                ('description', models.TextField()),
                ('price', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]