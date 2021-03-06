# Generated by Django 3.1.2 on 2020-10-12 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_feeding'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='feeding',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='feeding',
            name='date',
            field=models.DateField(verbose_name='fishing date'),
        ),
        migrations.AddField(
            model_name='puffin',
            name='rocks',
            field=models.ManyToManyField(to='main_app.Rock'),
        ),
    ]
