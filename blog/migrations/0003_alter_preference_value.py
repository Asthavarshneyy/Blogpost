# Generated by Django 4.1.5 on 2023-03-05 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_dislikes_post_likes_preference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='value',
            field=models.IntegerField(choices=[(0, 'Like'), (1, 'Dislike')]),
        ),
    ]
