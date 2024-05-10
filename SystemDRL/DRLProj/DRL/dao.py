from django.db.models import Count, F, Q
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
    condition = Q(thanhtichngoaikhoa__diem__gt=0)
    if req and (req.get('khoa') and req.get('khoa').strip() != '') or (req.get('lop') and req.get('lop').strip() != '') or (req.get('hk')):
        if req.get('khoa') is not None and req.get('khoa').strip() != '':
            condition &= Q(khoa__name__icontains=req.get('khoa'))
        if req.get('lop') is not None and req.get('lop').strip() != '':
            condition &= Q(lop__name__icontains=req.get('lop'))
        if req.get('hk') is not None and req.get('hk').strip() != '':
            condition &= Q(thanhtichngoaikhoa__hoc_ki__id=int(req.get('hk')))

    return UserSV.objects.annotate(diem=F('thanhtichngoaikhoa__diem')).filter(condition) \
        .values('mssv', 'first_name', 'last_name', 'diem').order_by(
        '-diem')


def TLSV_thong_ke(req):
    condition = Q(thanhtichngoaikhoa__diem__gt=0)
    if (req.get('lop') and req.get('lop').strip() != '') or (req.get('hk')) or (req.get('thanhtich') is not None and req.get('thanhtich').strip() != ''):
        if req.get('thanhtich') is not None and req.get('thanhtich').strip() != '':
            condition &= Q(thanhtichngoaikhoa__thanh_tich__icontains=req.get('thanhtich'))
        if req.get('lop') is not None and req.get('lop').strip() != '':
            condition &= Q(lop__name__icontains=req.get('lop'))
        if req.get('hk') is not None and req.get('hk').strip() != '':
            condition &= Q(thanhtichngoaikhoa__hoc_ki__id=int(req.get('hk')))

    return UserSV.objects.annotate(diem=F('thanhtichngoaikhoa__diem')).filter(condition) \
        .values('mssv', 'first_name', 'last_name', 'diem').order_by(
        '-diem')
