import csv
import json
from time import strftime

from django.contrib.auth.models import Group
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from rest_framework import viewsets, permissions, generics, status, parsers, serializers
from rest_framework.response import Response
from .models import HoatDong, Tag, Lop, Khoa, User, UserSV, QuyChe, ThanhTichNgoaiKhoa, Comment, Like, SinhVienMinhChungHoatDong, HocKi
from .serializer import HoatDongSerializerDetail, HocKiSerializer, KhoaSerializer, CommentSerializer, UserSVSerializer, HoatDongSerializer, LikeSerializer, LopSerializer, QuyCheSerializer, TagSerializer, ThanhTichNgoaiKhoaSerializer, UserSerializer, MinhChungSerializer
from .paginator import DRLPaginator
from .perms import HasGroupTLSVPermission
from django.templatetags.static import static
from django.conf import settings

# Create your views here.


class KhoaViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView, generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = Khoa.objects.all()
    serializer_class = KhoaSerializer
    pagination_class = DRLPaginator

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(name__icontains=q)
        return queries


class LopViewSet(viewsets.ViewSet, generics.ListAPIView):
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

    @action(methods=['GET'], detail=True)
    def hoat_dongs(self, request, pk):
        hd = self.get_object().hoat_dongs.filter(active=True)
        return Response(HoatDongSerializer(hd, many=True, context={
            'request': request
        }).data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def thanh_tichs(self, request, pk):
        tt = self.get_object().thanh_tich_ngoai_khoa
        return Response(ThanhTichNgoaiKhoaSerializer(tt, context={
            'request': request
        }).data, status=status.HTTP_200_OK)


class MinhChungViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = SinhVienMinhChungHoatDong.objects.all()
    serializer_class = MinhChungSerializer
    pagination_class = DRLPaginator
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    permission_classes = (HasGroupTLSVPermission, )
    required_groups = {
        'GET': ['TLSV'],
    }

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
        if self.action.__eq__('get_current'):
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    @action(methods=['post'], url_path="ctsv", detail=False)
    def add_ctsv(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = UserSerializer.create(self, serializer.validated_data)
        nhom = Group.objects.get(name='CTSV')
        user.groups.add(nhom)
        user.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

    @action(methods=['post'], url_path="tlsv", detail=False)
    def add_tlsv(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = UserSerializer.create(self, serializer.validated_data)
        nhom = Group.objects.get(name='TLSV')
        user.groups.add(nhom)
        user.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

    @action(methods=['get'], url_path="current", detail=False)
    def get_current(self, request):
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)


class HocKiViewSet(viewsets.ViewSet, generics.ListAPIView):
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
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get('q')
        if q:
            queries = queries.filter(name__icontains=q)
        return queries

    @action(methods=['POST'], url_path="diemdanh", detail=True)
    def diem_danh(self, request, pk):
        # headers = ['MSSV', 'First Name', 'Last Name', 'Email']
        file_name = f"{self.get_object().id}_{strftime('%Y-%m-%d-%H-%M')}"
        s = f"{settings.MEDIA_ROOT}/diem_danh/{file_name}.csv"

        with open(s, 'a+', newline='') as csv_file:
            write = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            line = [request.data.get('mssv'), request.data.get('first_name'), request.data.get('last_name'),
                    request.data.get('email')]
            # write.writerow(headers)
            write.writerow(line)

        # writer = csv.writer(response)
        # writer.writerow(headers)

        # users = UserSV.objects.values(request.data.get('mssv'), request.data.get('first_name'), request.data.get('last_name'), request.data.get('email'))

        return HttpResponse(status=200)

    # @action(methods=['POST'], url_path="diemdanh", detail=True)
    # def diem_danh(self, request, pk):
    #     headers = ['MSSV', 'First Name', 'Last Name', 'Email']
    #     file_name = f"{self.get_object().id}_{strftime('%Y-%m-%d-%H-%M')}"
    #
    #     response = HttpResponse(content_type='text/csv')
    #     response['Content-Disposition'] = f'attachment; filename="{file_name}.csv"'
    #
    #     writer = csv.writer(response)
    #     writer.writerow(headers)
    #
    #     # users = UserSV.objects.values(request.data.get('mssv'), request.data.get('first_name'), request.data.get('last_name'), request.data.get('email'))
    #
    #     line = [request.data.get('mssv'), request.data.get('first_name'), request.data.get('last_name'), request.data.get('email')]
    #     writer.writerow(line)
    #     return response


class QuyCheViewSet(viewsets.ViewSet, generics.ListAPIView):
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


class ThanhTichViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = ThanhTichNgoaiKhoa.objects.all()
    serializer_class = ThanhTichNgoaiKhoaSerializer
    pagination_class = DRLPaginator