# Generated by Django 4.2.11 on 2024-05-13 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DRL', '0020_remove_hoatdong_user_svs'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoatDong_SV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hoat_dong', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DRL.hoatdong')),
                ('sinh_vien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DRL.usersv')),
            ],
        ),
        migrations.AddField(
            model_name='hoatdong',
            name='user_svs',
            field=models.ManyToManyField(blank=True, through='DRL.HoatDong_SV', to='DRL.usersv'),
        ),
    ]