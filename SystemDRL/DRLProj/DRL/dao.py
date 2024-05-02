from django.db.models import Count, F
from .models import Khoa, UserSV


# def load_thanh_tich(params = {}):
#     q = ThanhTichNgoaiKhoa.objects.all()
#     kw = params.get('kw')
#     if kw:
#         q = q.objects.filter(name__icontains=kw)
#     cate = params.get('cate')
#     if cate:
#         q = q.objects.filter(category_id=cate)

def order_drl_by_khoa(name):
    if name is not None and name.strip() != '':
        return UserSV.objects.filter(khoa__name__icontains=name).annotate(diem=F('thanhtichngoaikhoa__diem'))\
            .values('mssv', 'first_name', 'last_name', 'diem').order_by('-diem')

    else:
        return UserSV.objects.annotate(diem=F('thanhtichngoaikhoa__diem')) \
            .values('mssv', 'first_name', 'last_name', 'diem').order_by(
            '-diem')
