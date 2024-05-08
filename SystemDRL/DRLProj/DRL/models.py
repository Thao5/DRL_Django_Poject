import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.utils.timezone import now

from DRLProj.settings import MEDIA_ROOT


# Create your models here.


class User(AbstractUser):
    avatar = CloudinaryField('avatar', null=True)
    phone = models.CharField(max_length=10, unique=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.set_password(self.password)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Người dùng"


class UserSV(User):
    mssv = models.CharField(max_length=10, unique=True, default='0000000000')
    ngay_sinh = models.DateField(default=datetime.date.today)
    ngay_nhap_hoc = models.DateField(default=datetime.date.today)
    khoa = models.ForeignKey('Khoa', on_delete=models.SET_NULL, null=True)
    lop = models.ForeignKey('Lop', on_delete=models.SET_NULL, null=True)
    # thanh_tich_ngoai_khoa = models.OneToOneField('ThanhTichNgoaiKhoa', on_delete=models.SET_NULL, null=True)
    # hoat_dongs = models.ManyToManyField('HoatDong', blank=True)

    class Meta:
        verbose_name = "Sinh viên"

    def save(self, *args, **kwargs):
        tmp = 0
        if self.mssv == "0000000000":
            tmp = UserSV.objects.all().count()
        if (tmp + 1) > 0 and self.mssv == "0000000000":
            self.mssv = f'{(tmp + 1):010}'
        super(UserSV, self).save(*args, **kwargs)


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
    hoc_ki = models.ForeignKey('HocKi', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hoạt động"


class Khoa(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Khoa"


class Lop(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Lớp"


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

    class Meta:
        verbose_name = "Quy chế"


class HocKi(BaseModel):
    name = models.CharField(max_length=100)
    nien_khoa = models.CharField(max_length=100)
    thoi_gian_bat_dau = models.DateField()
    thoi_gian_ket_thuc = models.DateField()

    def __str__(self):
        return f"{self.name}({self.nien_khoa})"

    class Meta:
        verbose_name = "Học kì"


class SinhVienMinhChungHoatDong(BaseModel):
    minh_chung = models.FileField(upload_to=f'{MEDIA_ROOT}minh_chung/')
    trang_thai = models.CharField(max_length=20)
    sinh_vien = models.ForeignKey(UserSV, on_delete=models.CASCADE)
    hoat_dong = models.ForeignKey(HoatDong, on_delete=models.CASCADE)
    nguoi_kiem_tra_minh_chung = models.ForeignKey(User, on_delete=models.CASCADE, related_name="nguoi_minh_chung_hoat_dong", null=True)

    def __str__(self):
        return f"{self.sinh_vien.last_name} {self.sinh_vien.first_name} {self.hoat_dong.hoc_ki.name}({self.hoat_dong.hoc_ki.nien_khoa})"

    class Meta:
        verbose_name = "Sinh viên minh chứng hoạt động"


class ThanhTichNgoaiKhoa(BaseModel):
    diem = models.FloatField(default=0)
    thanh_tich = models.CharField(max_length=15)
    # quy_ches = models.ManyToManyField('QuyChe')
    sinh_vien = models.OneToOneField(UserSV, on_delete=models.SET_NULL, null=True)
    hoc_ki = models.ForeignKey('HocKi', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.sinh_vien.last_name} {self.sinh_vien.first_name} {self.hoc_ki.name}({self.hoc_ki.nien_khoa})"

    class Meta:
        verbose_name = "Thành tích ngoại khóa"


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