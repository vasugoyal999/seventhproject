# Generated by Django 2.2.2 on 2019-11-07 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eyebook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.CharField(max_length=5)),
                ('like_username', models.CharField(max_length=20)),
            ],
        ),
    ]
