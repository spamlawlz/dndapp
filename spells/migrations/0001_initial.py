# Generated by Django 3.0.6 on 2020-06-02 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('higher_level', models.TextField()),
                ('components', models.CharField(max_length=5)),
                ('spell_range', models.CharField(max_length=50)),
                ('material', models.CharField(max_length=200)),
                ('ritual', models.BooleanField()),
                ('duration', models.CharField(max_length=50)),
                ('concentration', models.BooleanField()),
                ('casting_time', models.CharField(max_length=50)),
                ('level', models.IntegerField()),
                ('school', models.CharField(max_length=100)),
                ('classes', models.TextField()),
                ('subclasses', models.TextField()),
                ('saving_throw', models.CharField(choices=[('strength', 'Strength'), ('dexterity', 'Dexterity'), ('constitution', 'Constitution'), ('intelligence', 'Intelligence'), ('wisdom', 'Wisdom'), ('charisma', 'Charisma')], max_length=50)),
            ],
        ),
    ]
