# Generated by Django 4.1.5 on 2023-03-05 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_preference_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='value',
            field=models.IntegerField(choices=[(1, 'Like'), (2, 'Dislike')]),
        ),
    ]
