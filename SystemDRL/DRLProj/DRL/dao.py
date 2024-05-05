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

def order_drl_by_khoa(req):
    if req and req.get('khoa') or req.get('lop'):
        if req.get('khoa') is not None and req.get('khoa').strip() != '':
            return UserSV.objects.filter(khoa__name__icontains=req.get('khoa')).annotate(diem=F('thanhtichngoaikhoa__diem'))\
                .values('mssv', 'first_name', 'last_name', 'diem').order_by('-diem')
        if req.get('lop') is not None and req.get('lop').strip() != '':
            return UserSV.objects.filter(lop__name__icontains=req.get('lop')).annotate(
                diem=F('thanhtichngoaikhoa__diem')) \
                .values('mssv', 'first_name', 'last_name', 'diem').order_by('-diem')

    else:
        return UserSV.objects.annotate(diem=F('thanhtichngoaikhoa__diem')) \
            .values('mssv', 'first_name', 'last_name', 'diem').order_by(
            '-diem')
