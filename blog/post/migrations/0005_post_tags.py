# Generated by Django 2.2.9 on 2020-02-02 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20200126_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(default='all', max_length=1000),
            preserve_default=False,
        ),
    ]
