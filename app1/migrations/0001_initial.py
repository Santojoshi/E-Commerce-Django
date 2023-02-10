# Generated by Django 4.1.5 on 2023-01-14 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_category', models.CharField(max_length=50)),
                ('card_subcategory', models.CharField(max_length=50)),
                ('card_item', models.CharField(max_length=50)),
                ('card_desc', models.CharField(max_length=80)),
                ('card_price', models.IntegerField(default=0)),
                ('card_date', models.DateField()),
                ('card_image', models.ImageField(default='', upload_to='card/')),
            ],
        ),
    ]