# Generated by Django 3.0.4 on 2020-04-22 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ham_Operator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_sign', models.CharField(max_length=10, unique=True)),
                ('licence', models.TextField()),
                ('name', models.TextField()),
                ('address', models.TextField()),
                ('telephone', models.TextField()),
                ('rig', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]