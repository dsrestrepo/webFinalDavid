# Generated by Django 3.1 on 2020-12-08 21:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finalProject', '0010_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(choices=[('Statistics', 'Statistics'), ('Computer Science', 'Computer Science'), ('Data Science', 'Data Science'), ('Communications', 'Communications'), ('Social', 'Social'), ('other', 'other')], default='other', max_length=16, unique=True),
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
