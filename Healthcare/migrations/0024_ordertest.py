# Generated by Django 4.2.6 on 2024-07-01 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0023_remove_ordermedicine_bkash_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('address', models.TextField(blank=True, default='', null=True)),
                ('phone_number', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('payment_method', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('transaction_id', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.test')),
            ],
        ),
    ]
