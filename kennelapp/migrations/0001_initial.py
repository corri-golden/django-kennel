# Generated by Django 3.1.1 on 2020-09-25 01:04

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
            name='Caretaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Kennel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'kennel',
                'verbose_name_plural': 'kennels',
            },
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Specie', models.CharField(max_length=50)),
                ('Owner', models.CharField(max_length=50)),
                ('Admitted', models.CharField(max_length=50)),
                ('Caretaker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kennelapp.caretaker')),
                ('Location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kennelapp.kennel')),
            ],
            options={
                'verbose_name': 'cat',
                'verbose_name_plural': 'cats',
            },
        ),
        migrations.AddField(
            model_name='caretaker',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kennels', to='kennelapp.kennel'),
        ),
        migrations.AddField(
            model_name='caretaker',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]