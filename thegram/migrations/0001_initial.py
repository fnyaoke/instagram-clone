# Generated by Django 3.1.3 on 2020-11-24 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('bio', models.CharField(max_length=350)),
                ('profile_pic', models.ImageField(upload_to='ProfilePicture/')),
                ('profile_avatar', models.ImageField(upload_to='AvatorPicture/')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pictsagram/')),
                ('image_caption', models.CharField(max_length=700)),
                ('tag_someone', models.CharField(blank=True, max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image_likes', models.ManyToManyField(blank=True, default=False, related_name='likes', to='thegram.Profile')),
                ('imageuploader_profile', models.ForeignKey(blank=True, null='True', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_post', models.CharField(max_length=150)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to='thegram.profile')),
                ('commented_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thegram.image')),
            ],
        ),
    ]
