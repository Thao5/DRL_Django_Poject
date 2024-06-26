# Generated by Django 4.2.11 on 2024-05-04 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DRL', '0010_remove_usersv_thanh_tich_ngoai_khoa_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hoatdong',
            options={'verbose_name': 'Hoạt động'},
        ),
        migrations.AlterModelOptions(
            name='hocki',
            options={'verbose_name': 'Học kì'},
        ),
        migrations.AlterModelOptions(
            name='khoa',
            options={'verbose_name': 'Khoa'},
        ),
        migrations.AlterModelOptions(
            name='lop',
            options={'verbose_name': 'Lớp'},
        ),
        migrations.AlterModelOptions(
            name='quyche',
            options={'verbose_name': 'Quy chế'},
        ),
        migrations.AlterModelOptions(
            name='sinhvienminhchunghoatdong',
            options={'verbose_name': 'Sinh viên minh chứng hoạt động'},
        ),
        migrations.AlterModelOptions(
            name='thanhtichngoaikhoa',
            options={'verbose_name': 'Thành tích ngoại khóa'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Người dùng'},
        ),
        migrations.AlterModelOptions(
            name='usersv',
            options={'verbose_name': 'Sinh viên'},
        ),
        migrations.RemoveField(
            model_name='thanhtichngoaikhoa',
            name='quy_ches',
        ),
    ]
