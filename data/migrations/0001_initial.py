# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TempUserOpinions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('opinion', models.CharField(max_length=64)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=128, blank=True)),
                ('opinionOwner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TempUserQueries',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=64)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=128, blank=True)),
                ('queryOwner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserOpinionDislike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('dislikeUser', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserOpinionIrrelevant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('irrelevantUser', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserOpinionLikes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('likeUser', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserOpinions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('opinion', models.CharField(max_length=64)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=128, blank=True)),
                ('opinionOwner', models.ForeignKey(related_name='userOpinionOwner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserOpinionTagMapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('opinion', models.ForeignKey(to='data.UserOpinions')),
            ],
        ),
        migrations.CreateModel(
            name='UserQueries',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=64)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=128, blank=True)),
                ('queryOwner', models.ForeignKey(related_name='userQueryOwner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserQueryComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('commentText', models.CharField(max_length=128, blank=True)),
                ('commentOwner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(to='data.UserQueries')),
            ],
        ),
        migrations.CreateModel(
            name='UserQueryTagMapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.ForeignKey(to='data.UserQueries')),
            ],
        ),
        migrations.CreateModel(
            name='UserTags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='userquerytagmapping',
            name='tag',
            field=models.ForeignKey(to='data.UserTags'),
        ),
        migrations.AddField(
            model_name='useropiniontagmapping',
            name='tag',
            field=models.ForeignKey(to='data.UserTags'),
        ),
        migrations.AddField(
            model_name='useropinions',
            name='questionOfOpinion',
            field=models.ForeignKey(related_name='parentUserQuery', to='data.UserQueries'),
        ),
        migrations.AddField(
            model_name='useropinionlikes',
            name='opinionLiked',
            field=models.ForeignKey(to='data.UserOpinions'),
        ),
        migrations.AddField(
            model_name='useropinionirrelevant',
            name='opinion',
            field=models.ForeignKey(to='data.UserOpinions'),
        ),
        migrations.AddField(
            model_name='useropiniondislike',
            name='opinion',
            field=models.ForeignKey(to='data.UserOpinions'),
        ),
        migrations.AddField(
            model_name='tempuseropinions',
            name='questionOfOpinion',
            field=models.ForeignKey(to='data.TempUserQueries'),
        ),
    ]
