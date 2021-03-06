# Generated by Django 2.0.4 on 2018-04-08 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deputat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vrd_link', models.URLField()),
                ('vrd_id', models.IntegerField(blank=True, null=True)),
                ('vrd_photo', models.URLField()),
                ('surname', models.CharField(blank=True, default='', max_length=64, null=True)),
                ('name', models.CharField(blank=True, default='', max_length=64, null=True)),
                ('patronymic', models.CharField(blank=True, default='', max_length=64, null=True)),
                ('selected_by', models.CharField(blank=True, default='', max_length=128, null=True)),
                ('party', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('party_number', models.IntegerField(blank=True, null=True)),
                ('fraction', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('position', models.CharField(blank=True, default='', max_length=512, null=True)),
                ('region', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('gender', models.CharField(blank=True, default='', max_length=1, null=True)),
            ],
            options={
                'verbose_name': 'Deputat',
                'verbose_name_plural': 'Deputats',
            },
        ),
    ]
