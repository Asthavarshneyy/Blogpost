# Generated by Django 4.1.5 on 2023-01-21 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_rename_body_post_blog_post_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='owner',
            new_name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
