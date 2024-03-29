# Generated by Django 3.1.1 on 2021-04-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manuals', '0008_auto_20200825_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manuals',
            name='format',
            field=models.CharField(blank=True, choices=[('.pdf', 'PDF'), ('.doc', 'Ms Word <2017'), ('.docx', 'Ms Word >2017'), ('.jpg', 'JPEG Image File')], default='.pdf', help_text='Document Type/Format', max_length=6),
        ),
    ]
