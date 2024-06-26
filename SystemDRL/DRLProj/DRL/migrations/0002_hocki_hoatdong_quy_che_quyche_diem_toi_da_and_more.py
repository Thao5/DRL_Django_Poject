# Generated by Django 4.2.11 on 2024-04-16 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DRL', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HocKi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
                ('nien_khoa', models.CharField(max_length=100)),
                ('thoi_gian_bat_dau', models.DateField()),
                ('thoi_gian_ket_thuc', models.DateField()),
            ],
            options={
                'ordering': ['id'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='hoatdong',
            name='quy_che',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='DRL.quyche'),
        ),
        migrations.AddField(
            model_name='quyche',
            name='diem_toi_da',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='usersv',
            name='mssv',
            field=models.CharField(default='0000000000', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
