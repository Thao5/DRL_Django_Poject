from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField

# Create your models here.


class User(AbstractUser):
    avatar = CloudinaryField('avatar', null=True)
    phone = models.CharField(max_length=10, unique=True, null=True)


class UserSV(User):
    mssv = models.CharField(max_length=10, unique=True, default='0000000000')
    khoa = models.ForeignKey('Khoa', on_delete=models.SET_NULL, null=True)
    lop = models.ForeignKey('Lop', on_delete=models.SET_NULL, null=True)
    thanh_tich_ngoai_khoa = models.OneToOneField('ThanhTichNgoaiKhoa', on_delete=models.SET_NULL, null=True)
    # hoat_dongs = models.ManyToManyField('HoatDong', blank=True)


class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['id']


class HoatDong(BaseModel):
    name = models.CharField(max_length=100)
    mo_ta = RichTextField()
    ngay_du_kien = models.DateField()
    ngay_dien_ra = models.DateField()
    ngay_het = models.DateField()
    diem_cong = models.FloatField(default=0)
    tags = models.ManyToManyField('Tag')
    quy_che = models.ForeignKey('QuyChe', on_delete=models.SET_NULL, null=True)
    user_svs = models.ManyToManyField('UserSV', blank=True)


    def __str__(self):
        return self.name


class Khoa(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Lop(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class QuyChe(BaseModel):
    name = models.CharField(max_length=100)
    mo_ta = RichTextField()
    diem_toi_da = models.FloatField(default=0)

    def __str__(self):
        return self.name


class HocKi(BaseModel):
    name = models.CharField(max_length=100)
    nien_khoa = models.CharField(max_length=100)
    thoi_gian_bat_dau = models.DateField()
    thoi_gian_ket_thuc = models.DateField()


class SinhVienMinhChungHoatDong(BaseModel):
    minh_chung = models.FileField()
    trang_thai = models.CharField(max_length=20)
    sinh_vien = models.ForeignKey(UserSV, on_delete=models.CASCADE)
    hoat_dong = models.ForeignKey(HoatDong, on_delete=models.CASCADE)


class ThanhTichNgoaiKhoa(BaseModel):
    diem = models.FloatField(default=0)
    thanh_tich = models.CharField(max_length=15)
    quy_ches = models.ManyToManyField('QuyChe')


class Interaction(BaseModel):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    hoat_dong = models.ForeignKey(HoatDong, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Comment(Interaction):
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content


class Like(Interaction):
    is_like = models.BooleanField(default=True)

    class Meta:
        unique_together = ('user', 'hoat_dong')