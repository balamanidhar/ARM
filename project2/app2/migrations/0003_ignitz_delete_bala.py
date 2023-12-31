# Generated by Django 4.1.2 on 2023-08-30 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_bala_delete_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ignitz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Candidate_Name', models.CharField(max_length=50)),
                ('Father_Name', models.CharField(max_length=50)),
                ('Referred_By', models.CharField(max_length=50)),
                ('Date_Of_Birth', models.DateField()),
                ('Mobile_number', models.IntegerField()),
                ('Email_Id', models.EmailField(max_length=254)),
                ('Hometown', models.CharField(max_length=50)),
                ('Qualification', models.CharField(max_length=50)),
                ('College_name', models.CharField(max_length=100)),
                ('Stream', models.CharField(max_length=50)),
                ('Btech_Percentage', models.IntegerField()),
                ('Passed_out_year', models.IntegerField()),
                ('Any_Backlogs', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='bala',
        ),
    ]
