# Generated by Django 3.2.5 on 2021-08-06 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_usuario_opiniao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='email',
        ),
        migrations.AddField(
            model_name='usuario',
            name='desing',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='usuario',
            name='perguntas',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='usuario',
            name='videos',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(default='', max_length=255),
        ),
    ]
