# Generated by Django 2.2 on 2020-05-28 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_question_replied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='question',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.Question'),
        ),
    ]
