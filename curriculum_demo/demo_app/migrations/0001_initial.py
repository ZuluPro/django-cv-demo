# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResumes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resumes', models.ManyToManyField(to='curriculum.Resume')),
                ('user', models.ForeignKey(verbose_name='user', to=settings.AUTH_USER_MODEL, help_text='User associated with resume.', unique=True)),
            ],
        ),
    ]
