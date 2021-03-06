# Generated by Django 3.1.5 on 2021-01-25 07:22

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
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False)),
                ('title', models.CharField(max_length=15)),
                ('content', models.TextField(blank=True)),
                ('hash_tag', models.CharField(blank=True, max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('dis_like', models.ManyToManyField(related_name='dis_likes', to=settings.AUTH_USER_MODEL)),
                ('like', models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '비디오들',
                'verbose_name_plural': '비디오',
                'db_table': 'video',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('follower', models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '팔로우들',
                'verbose_name_plural': '팔로우',
                'db_table': 'follow',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('is_deleted', models.BooleanField(blank=True, default=False)),
                ('content', models.CharField(max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.video')),
            ],
            options={
                'verbose_name': '댓글들',
                'verbose_name_plural': '댓글',
                'db_table': 'comment',
                'ordering': ('-created',),
            },
        ),
    ]
