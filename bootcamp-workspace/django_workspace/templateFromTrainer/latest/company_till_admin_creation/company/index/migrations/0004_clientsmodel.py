# Generated by Django 5.1 on 2024-08-26 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_alter_pricingmodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(max_length=100)),
                ('clientLink', models.CharField(max_length=300)),
                ('clientLogo', models.ImageField(upload_to='clientLogos/')),
            ],
        ),
    ]
