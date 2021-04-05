# Generated by Django 3.1.7 on 2021-04-05 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todolist_task_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='priority',
            field=models.CharField(choices=[(1, 'High'), (2, 'Moderate'), (3, 'Low')], default='Moderate', max_length=10),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='task',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
