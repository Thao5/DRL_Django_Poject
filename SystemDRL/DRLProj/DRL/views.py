import csv
import json
from collections import defaultdict
from time import strftime

from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import upper
from drf_yasg.utils import swagger_auto_schema
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Table, TableStyle
from reportlab.rl_settings import defaultPageSize
from rest_framework.decorators import action
from rest_framework import viewsets, permissions, generics, status, parsers, serializers
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .models import HoatDong, Tag, Lop, Khoa, User, UserSV, QuyChe, ThanhTichNgoaiKhoa, Comment, Like, SinhVienMinhChungHoatDong, HocKi
from .serializer import HoatDongSerializerDetail, HocKiSerializer, KhoaSerializer, CommentSerializer, UserSVSerializer, HoatDongSerializer, LikeSerializer, LopSerializer, QuyCheSerializer, TagSerializer, ThanhTichNgoaiKhoaSerializer, UserSerializer, MinhChungSerializer
from .paginator import DRLPaginator
from .perms import HasGroupTLSVPermission
from django.templatetags.static import static
from django.conf import settings
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from .dao import order_drl_by_khoa, tlsv_thong_ke
from .perms import is_in_group, HasGroupPermission
from .admin import DRLAppAdminSite


# Create your views here.


class KhoaViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Khoa.objects.all()
    serializer_class = KhoaSerializer
    pagination_class = DRLPaginator

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(name__icontains=q)
        return queries


class LopViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Lop.objects.all()
    serializer_class = LopSerializer
    pagination_class = DRLPaginator

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(name__icontains=q)
        return queries


class UserSVViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView, generics.CreateAPIView):
    queryset = UserSV.objects.all()
    serializer_class = UserSVSerializer
    pagination_class = DRLPaginator
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(mssv__icontains=q)
        return queries

    def create(self, request, *args, **kwargs):
        nhom = Group.objects.get(name='SV')
        serializer = UserSVSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user_sv = UserSVSerializer.create(self, serializer.validated_data)
            user_sv.full_clean()
            user_sv.save()
            user_sv.groups.add(nhom)
            user_sv.save()
            return Response(UserSVSerializer(user_sv).data, status=status.HTTP_201_CREATED)
        except ValidationError:
            return Response(None, status=status.HTTP_400_BAD_REQUEST)

    # def create(self, request, *args, **kwargs):
    #     uploaded_file = request.FILES['avatar']
    #     filename = uploaded_file.name
    #     serializer = UserSVSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = UserSVSerializer.create(self, serializer.validated_data)
    #     user.avatar = filename
    #     user.save()
    #     return super(UserSVViewSet, self).create(request, *args, **kwargs)

    @action(methods=['GET'], detail=True)
    def hoat_dongs(self, request, pk):
        hd = self.get_object().hoatdong_set.filter(active=True)
        return Response(HoatDongSerializer(hd, many=True, context={
            'request': request
        }).data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def thanh_tichs(self, request, pk):
        tt = self.get_object().thanhtichngoaikhoa_set.filter(active=True)
        return Response(ThanhTichNgoaiKhoaSerializer(tt, many=True, context={
            'request': request
        }).data, status=status.HTTP_200_OK)


class MinhChungViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = SinhVienMinhChungHoatDong.objects.all()
    serializer_class = MinhChungSerializer
    pagination_class = DRLPaginator
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, JSONParser]
    permission_classes = (HasGroupTLSVPermission, )
    required_groups = {
        'GET': ['TLSV', 'CTSV', 'SV'],
        'POST': ['SV'],
        'PATCH': ['TLSV', 'CTSV']
    }

    # def patch(self, request, *args, **kwargs):
    #     mc = SinhVienMinhChungHoatDong.objects.get(pk=request.data.get('id'))
    #     u = User.objects.get(username=request.user.username)
    #     print(f'u: {u}')
    #     mc.nguoi_kiem_tra_minh_chung = u
    #     if mc.trang_thai == "Đã xử lý":
    #         print(mc.trang_thai)
    #         mc.hoat_dong.user_svs.add(mc.sinh_vien)
    #     mc.save()
    #
    #     return Response(MinhChungSerializer(mc).data, status=status.HTTP_200_OK)

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(sinh_vien__khoa__name__icontains=q)
        return queries


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def get_permissions(self):
        if self.action in ['get_current']:
            return [permissions.IsAuthenticated()]
        if self.action in ['add_ctsv', 'add_tlsv']:
            return [HasGroupPermission()]
        return [permissions.AllowAny()]

    @action(methods=['post'], url_path="ctsv", detail=False)
    def add_ctsv(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = UserSerializer.create(self, serializer.validated_data)
        nhom = Group.objects.get(name='CTSV')
        user.groups.add(nhom)
        user.is_staff = True
        user.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

    @action(methods=['post'], url_path="tlsv", detail=False)
    def add_tlsv(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = UserSerializer.create(self, serializer.validated_data)
        nhom = Group.objects.get(name='TLSV')
        user.groups.add(nhom)
        user.is_staff = True
        user.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

    @action(methods=['get'], url_path="current", detail=False)
    def get_current(self, request):
        u = User.objects.get(username=request.user)
        if is_in_group(u, "SV"):
            usv = UserSV.objects.get(username=u.username)
            return Response(UserSVSerializer(usv).data, status=status.HTTP_200_OK)
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)


class HocKiViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = HocKi.objects.all()
    serializer_class = HocKiSerializer
    pagination_class = DRLPaginator

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(name__icontains=q)
        return queries


class HoatDongViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView, generics.RetrieveAPIView):
    queryset = HoatDong.objects.all()
    serializer_class = HoatDongSerializerDetail
    pagination_class = DRLPaginator
    parser_classes = [parsers.MultiPartParser, parsers.FormParser, JSONParser]
    # hd_dict = defaultdict(list)

    def get_permissions(self):
        if self.action in ['add_comment', 'add_like', 'sinh_vien_dang_ky']:
            return [permissions.IsAuthenticated()]
        if self.action in ['diem_danh', 'diem_danh_tong_ket']:
            return [HasGroupPermission()]
        return [permissions.AllowAny()]

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(name__icontains=q)
        return queries

    @action(methods=['POST'], url_path="sinhviendangky", detail=True)
    def sinh_vien_dang_ky(self, request, pk):
        hd = self.get_object()
        u = User.objects.get(username=request.user.username)

        if is_in_group(u, "SV"):
            u = UserSV.objects.get(username=u.username)
            hd.user_svs.add(u)
        return Response(HoatDongSerializer(hd, context={
            'request': request
        }).data, status=status.HTTP_200_OK)

    @action(methods=['POST'], url_path="diemdanh", detail=True)
    def diem_danh(self, request, pk):
        # headers = ['MSSV', 'First Name', 'Last Name', 'Email']
        try:
            sv = UserSV.objects.get(mssv=request.data.get('mssv'))
            if DRLAppAdminSite.hd_dict.get(self.get_object().id) is None or UserSVSerializer(sv).data not in DRLAppAdminSite.hd_dict.get(self.get_object().id):
                DRLAppAdminSite.hd_dict[self.get_object().id].append(UserSVSerializer(sv).data)
        except UserSV.DoesNotExist:
            return Response(DRLAppAdminSite.hd_dict, status=status.HTTP_400_BAD_REQUEST)
        # file_name = f"{self.get_object().id}_{strftime('%Y-%m-%d-%H-%M')}"
        # s = f"{settings.MEDIA_ROOT}/diem_danh/{file_name}.csv"
        #
        # with open(s, 'a+', newline='', encoding='utf8') as csv_file:
        #     write = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        #     line = [request.data.get('mssv'), request.data.get('first_name'), request.data.get('last_name'),
        #             request.data.get('email')]
        #     # write.writerow(headers)
        #     write.writerow(line)
        #
        # # writer = csv.writer(response)
        # # writer.writerow(headers)
        #
        # # users = UserSV.objects.values(request.data.get('mssv'), request.data.get('first_name'), request.data.get('last_name'), request.data.get('email'))
        return Response(DRLAppAdminSite.hd_dict, status=status.HTTP_200_OK)

    @action(methods=['POST'], url_path="diemdanhtongket", detail=True)
    def diem_danh_tong_ket(self, request, pk):
        # headers = ['MSSV', 'First Name', 'Last Name', 'Email']
        hd = self.get_object()
        if DRLAppAdminSite.hd_dict.get(hd.id) is not None:
            for sv in DRLAppAdminSite.hd_dict[hd.id]:
                user_sv = UserSV.objects.get(pk=int(sv.get('id')))
                hd.user_svs.add(user_sv)
                DRLAppAdminSite.hd_dict[hd.id].remove(sv)
            hd.save()
        # file_name = f"{self.get_object().id}_{strftime('%Y-%m-%d-%H-%M')}"
        # s = f"{settings.MEDIA_ROOT}/diem_danh/{file_name}.csv"
        #
        # with open(s, 'a+', newline='', encoding='utf8') as csv_file:
        #     write = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        #     line = [request.data.get('mssv'), request.data.get('first_name'), request.data.get('last_name'),
        #             request.data.get('email')]
        #     # write.writerow(headers)
        #     write.writerow(line)
        #
        # # writer = csv.writer(response)
        # # writer.writerow(headers)
        #
        # # users = UserSV.objects.values(request.data.get('mssv'), request.data.get('first_name'), request.data.get('last_name'), request.data.get('email'))

        return Response(HoatDongSerializer(hd, context={
            'request': request
        }).data, status=status.HTTP_200_OK)

    @action(methods=['GET'], url_path="diemdanhcsv", detail=True)
    def diem_danh_csv(self, request, pk):
        headers = ['MSSV', 'First Name', 'Last Name', 'Email']
        file_name = f"{self.get_object().id}_{strftime('%Y-%m-%d-%H-%M')}"
        s = f"{settings.MEDIA_ROOT}/diem_danh/{file_name}.csv"

        with open(s, 'a+', newline='', encoding='utf8') as csv_file:
            write = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            line=[]
            for sv in DRLAppAdminSite.hd_dict[self.get_object().id]:
                line = [sv.get('mssv'), sv.get('first_name'), sv.get('last_name'),
                        sv.get('email')]
                write.writerow(line)
            # write.writerow(headers)


        # writer = csv.writer(response)
        # writer.writerow(headers)

        # # users = UserSV.objects.values(request.data.get('mssv'), request.data.get('first_name'), request.data.get('last_name'), request.data.get('email'))
        return Response(DRLAppAdminSite.hd_dict, status=status.HTTP_200_OK)

    @action(methods=['POST'], url_path="addcomment", detail=True)
    def add_comment(self, request, pk):
        comment = Comment()
        comment.hoat_dong = self.get_object()
        comment.content = request.data.get('content')
        comment.user = request.user
        comment.save()
        return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)

    @action(methods=['POST'], url_path="addlike", detail=True)
    def add_like(self, request, pk):
        try:
            like = Like.objects.get(user_id=User.objects.get(username=request.user.username).id, hoat_dong_id=self.get_object().id)
        except Like.DoesNotExist:
            like = None
        if like:
            like.is_like = not like.is_like
            like.save()
            return Response(LikeSerializer(like).data, status=status.HTTP_200_OK)
        else:
            like = Like()
            like.hoat_dong = self.get_object()
            like.user = request.user
            like.save()
        return Response(LikeSerializer(like).data, status=status.HTTP_201_CREATED)


class QuyCheViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = QuyChe.objects.all()
    serializer_class = QuyCheSerializer
    pagination_class = DRLPaginator

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(name__icontains=q)
        return queries


class CommentViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = DRLPaginator

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(content__icontains=q)
        return queries


class LikeViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    pagination_class = DRLPaginator


class TagViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = DRLPaginator

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(name__icontains=q)
        return queries


class ThanhTichViewSet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = ThanhTichNgoaiKhoa.objects.all()
    serializer_class = ThanhTichNgoaiKhoaSerializer
    pagination_class = DRLPaginator

    def get_permissions(self):
        if self.action in ['thong_ke', 'thong_ke_tlsv', 'StatsPDF', 'StatsCSV', 'StatsPDF_tlsv', 'StatsCSV_tlsv']:
            return [HasGroupPermission()]
        return [permissions.AllowAny()]

    @action(methods=['GET'], url_path="thongke", detail=False)
    def thong_ke(self, request):
        return Response(order_drl_by_khoa(self.request.query_params), status=status.HTTP_200_OK)

    @action(methods=['GET'], url_path="thongketlsv", detail=False)
    def thong_ke_tlsv(self, request):
        return Response(tlsv_thong_ke(self.request.query_params), status=status.HTTP_200_OK)

    @action(methods=['GET'], url_path="statspdf", detail=False)
    def StatsPDF(self, request):
        pdfmetrics.registerFont(TTFont("Vera", "Vera.ttf"))  # <- Important
        pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
        drls = order_drl_by_khoa(self.request.query_params)
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
        text = u"THỐNG KÊ ĐIỂM RÈN LUYỆN"
        tmp = ''
        if self.request.query_params.get('khoa') and self.request.query_params.get('khoa').strip() != '':
            tmp += u' THEO KHOA {}'.format(self.request.query_params.get('khoa'))
        if self.request.query_params.get('lop') and self.request.query_params.get('lop').strip() != '':
            tmp += u' THEO LỚP {}'.format(self.request.query_params.get('lop'))
        if self.request.query_params.get('hk') and self.request.query_params.get('hk').strip() != '':
            h = HocKi.objects.get(id=int(self.request.query_params.get('hk')))
            tmp += u' THEO {}({})'.format(upper(h.name), h.nien_khoa)
        if self.request.query_params.get('thanhtich') and self.request.query_params.get('thanhtich').strip() != '':
            tmp += u' THEO THÀNH TÍCH {}'.format(self.request.query_params.get('thanhtich').strip())
        text = u'{}{}'.format(text, tmp)
        text_width = stringWidth(text, fontName="Vera", fontSize=14)
        font_size=14
        if text_width > 600:
            font_size = 10
        textob = c.beginText()
        textob.setTextOrigin(inch, inch)
        textob.setFont("Vera", font_size)
        c.setFont("Verdana", font_size)

        t = [['MSSV', 'Họ', 'Tên', 'Điểm']]

        for d in drls:
            t.append([d.get('mssv'), d.get('last_name'), d.get('first_name'), str(d.get('diem'))])

        t = t[::-1]
        c.drawCentredString(330, inch, text)
        c.drawText(textob)
        f = Table(t, rowHeights=inch)
        f.setStyle(TableStyle([('FONTNAME', (0, 0), (-1, -1), "Verdana"),
                               ('INNERGRID', (0, 0), (-1, -1), 0, colors.black),
                               ('BOX', (0, 0), (-1, -1), 0, colors.black),
                               ('ALIGN', (0, 0), (-1, -1), "CENTER"),
                               ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        f.wrapOn(c, c._pagesize[0], c._pagesize[1])
        f.drawOn(c, inch, inch + 20)
        c.showPage()
        c.save()
        buf.seek(0)
        return FileResponse(buf, as_attachment=True, filename="statsPDF.pdf")

    @action(methods=['GET'], url_path="statspdftlsv", detail=False)
    def StatsPDF_tlsv(self, request):
        pdfmetrics.registerFont(TTFont("Vera", "Vera.ttf"))  # <- Important
        pdfmetrics.registerFont(TTFont('Verdana', 'Verdana.ttf'))
        drls = tlsv_thong_ke(self.request.query_params)
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
        text = u"THỐNG KÊ ĐIỂM RÈN LUYỆN"
        tmp = ''
        if self.request.query_params.get('thanhtich') and self.request.query_params.get('thanhtich').strip() != '':
            tmp += u' THEO THÀNH TÍCH {}'.format(self.request.query_params.get('thanhtich'))
        if self.request.query_params.get('lop') and self.request.query_params.get('lop').strip() != '':
            tmp += u' THEO LỚP {}'.format(self.request.query_params.get('lop'))
        if self.request.query_params.get('hk') and self.request.query_params.get('hk').strip() != '':
            h = HocKi.objects.get(id=int(self.request.query_params.get('hk')))
            tmp += u' THEO {}({})'.format(upper(h.name), h.nien_khoa)
        if self.request.query_params.get('thanhtich') and self.request.query_params.get('thanhtich').strip() != '':
            tmp += u' THEO THÀNH TÍCH {}'.format(self.request.query_params.get('thanhtich').strip())
        text = u'{}{}'.format(text, tmp)
        text_width = stringWidth(text, fontName="Vera", fontSize=14)
        font_size = 14
        if text_width > 600:
            font_size = 10
        textob = c.beginText()
        textob.setTextOrigin(inch, inch)
        textob.setFont("Vera", font_size)
        c.setFont("Verdana", font_size)

        t = [['MSSV', 'Họ', 'Tên', 'Điểm']]

        for d in drls:
            t.append([d.get('mssv'), d.get('last_name'), d.get('first_name'), str(d.get('diem'))])

        t = t[::-1]
        c.drawCentredString(330, inch, text)
        c.drawText(textob)
        f = Table(t, rowHeights=inch)
        f.setStyle(TableStyle([('FONTNAME', (0, 0), (-1, -1), "Verdana"),
                               ('INNERGRID', (0, 0), (-1, -1), 0, colors.black),
                               ('BOX', (0, 0), (-1, -1), 0, colors.black),
                               ('ALIGN', (0, 0), (-1, -1), "CENTER"),
                               ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')]))
        f.wrapOn(c, c._pagesize[0], c._pagesize[1])
        f.drawOn(c, inch, inch + 20)
        c.showPage()
        c.save()
        buf.seek(0)
        return FileResponse(buf, as_attachment=True, filename="statsPDF.pdf")

    @action(methods=['GET'], url_path="statscsv", detail=False)
    def StatsCSV(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="statsCSV.csv"'

        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response)
        writer.writerow(["MSSV", "Last name", "First name", "diem"])
        drls = order_drl_by_khoa(self.request.query_params)
        for d in drls:
            writer.writerow([f"'{d.get('mssv')}", d.get('last_name'), d.get('first_name'), str(d.get('diem'))])

        return response

    @action(methods=['GET'], url_path="statscsvtlsv", detail=False)
    def StatsCSV_tlsv(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="statsCSV.csv"'

        response.write(u'\ufeff'.encode('utf8'))
        writer = csv.writer(response)
        writer.writerow(["MSSV", "Last name", "First name", "diem"])
        drls = tlsv_thong_ke(self.request.query_params)
        for d in drls:
            writer.writerow([f"'{d.get('mssv')}", d.get('last_name'), d.get('first_name'), str(d.get('diem'))])

        return response





