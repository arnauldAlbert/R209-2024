# Generated by Django 5.0.4 on 2024-04-15 14:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('page_number', models.IntegerField()),
                ('editing_date', models.DateField()),
                ('summary', models.TextField(blank=True, null=True)),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliotheque.categorie')),
            ],
        ),
    ]
