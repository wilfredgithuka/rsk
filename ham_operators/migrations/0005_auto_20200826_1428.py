# Generated by Django 3.0.3 on 2020-08-26 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ham_operators', '0004_auto_20200826_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='operator',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='operator',
            name='nationality',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='operator',
            name='telephone',
            field=models.CharField(max_length=20),
        ),
    ]
