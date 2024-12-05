# Generated by Django 5.1.4 on 2024-12-05 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bankloan',
            fields=[
                ('LOAN_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('CUST_NAME', models.CharField(max_length=100)),
                ('LOAN_TYPE', models.CharField(max_length=100)),
                ('CUST_ACNO', models.IntegerField()),
                ('LOAN_AMT', models.IntegerField()),
            ],
        ),
    ]