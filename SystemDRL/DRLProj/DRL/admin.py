from collections import defaultdict

from django.contrib import admin
from django import forms
from django.contrib.auth import authenticate
from django.middleware.csrf import get_token
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.html import mark_safe
from django.contrib.auth.models import Permission, Group
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions

from .models import HoatDong, Tag, Lop, Khoa, User, UserSV, QuyChe, ThanhTichNgoaiKhoa, Comment, Like, SinhVienMinhChungHoatDong, HocKi
from .dao import order_drl_by_khoa
from .perms import HasGroupPermission, is_in_group, is_in_group_admin
from .serializer import UserSVSerializer


# Register your models here.


class DRLAppAdminSite(admin.AdminSite):
    site_header = "TRANG QUẢN TRỊ HỆ THỐNG ĐÁNG GIÁ ĐIỂM RÈN LUYỆN"
    index_title = "TRANG QUẢN TRỊ HỆ THỐNG ĐÁNG GIÁ ĐIỂM RÈN LUYỆN"
    hd_dict = defaultdict(list)

    def has_permission(self, request):
        # try:
        #     u = User.objects.get(username=request.user.username)
        #     return is_in_group(u, "TLSV") or is_in_group(u, "CTSV") or u.is_staff
        # except User.DoesNotExist:
        #     return request.user.is_anonymous
        # return (is_in_group_admin(request, "TLSV") or is_in_group_admin(request, "CTSV") or request.user.is_staff or request.user.is_superuser) and request.user.is_active
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            request.user = user
            print(request.user)
            return (is_in_group_admin(user, "TLSV") or is_in_group_admin(user, "CTSV") or request.user.is_staff or request.user.is_superuser) and (request.user.is_active or user.is_active)
        return request.user.is_active

    def get_urls(self):
        return [
                   path('drl-stats/', self.stats_view),
                    path('drl-diemdanh/', self.diem_danh_view),
                    # path('sentiment/', self.sentiment_view),
               ] + super().get_urls()

    # def sentiment_view(self, request):
    #     return TemplateResponse(request, 'admin/sentiment.html', {
    #     })

    def stats_view(self, request):
        stats = order_drl_by_khoa(request.GET)
        khoas = Khoa.objects.all()
        lops = Lop.objects.all()
        hks = HocKi.objects.all()
        return TemplateResponse(request, 'admin/stats_view.html',{
            'stats': stats,
            'site_header': DRLAppAdminSite.site_header,
            'index_title': 'STATS',
            'khoas': khoas,
            'lops': lops,
            'hks': hks
        })

    @csrf_exempt
    def diem_danh_view(self, request):
        csrf_token = get_token(request)
        hd_id = request.POST.get('hd_id')
        try:
            sv = UserSV.objects.get(mssv=request.POST.get('mssv'))
            if hd_id is not None and hd_id.strip() != '':
                if DRLAppAdminSite.hd_dict.get(int(hd_id)) is None or UserSVSerializer(sv).data not in DRLAppAdminSite.hd_dict.get(int(hd_id)):
                    DRLAppAdminSite.hd_dict[int(hd_id)].append(UserSVSerializer(sv).data)
        except UserSV.DoesNotExist:
            sv = None
        diem_danhs = list(DRLAppAdminSite.hd_dict.values())
        hds = HoatDong.objects.all()
        search_hds = []
        for dd in DRLAppAdminSite.hd_dict:
            search_hds.append(HoatDong.objects.get(pk=int(dd)))
        if request.GET.get('search_hd_id') is not None and request.GET.get('search_hd_id').strip() != '':
            diem_danhs = [DRLAppAdminSite.hd_dict[int(request.GET.get('search_hd_id'))]]

        if request.GET.get('tongket') is not None and request.GET.get('tongket').strip() != '' and request.GET.get('tongket') == '1':
            print()
            if DRLAppAdminSite.hd_dict.get(int(request.GET.get('search_hd_id'))) is not None:
                hd = HoatDong.objects.get(pk=int(request.GET.get('search_hd_id')))
                for sv in DRLAppAdminSite.hd_dict[int(request.GET.get('search_hd_id'))]:
                    user_sv = UserSV.objects.get(pk=int(sv.get('id')))
                    hd.user_svs.add(user_sv)
                    DRLAppAdminSite.hd_dict[int(request.GET.get('search_hd_id'))].remove(sv)
                hd.save()

        return TemplateResponse(request, 'admin/diemdanh.html',{
            'dds': diem_danhs,
            'hds': hds,
            'search_hds': search_hds,
            "csrf_token": csrf_token,
        })


class HoatDongTagInlineAdmin(admin.TabularInline):
    model = HoatDong.tags.through


class HoatDongForm(forms.ModelForm):
    mo_ta = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = HoatDong
        fields = '__all__'


class HoatDongAdmin(admin.ModelAdmin):
    list_display = [hd.name for hd in HoatDong._meta.fields]
    list_filter = ['id', 'name']
    search_fields = ['name']
    form = HoatDongForm
    inlines = [HoatDongTagInlineAdmin]

    def has_module_permission(self, request):
        return True


class SinhVienMinhChungAdmin(admin.ModelAdmin):
    list_display = [l.name for l in SinhVienMinhChungHoatDong._meta.fields]
    list_filter = ['id']
    readonly_fields = ('nguoi_kiem_tra_minh_chung',)

    def save_model(self, request, obj, form, change):
        u = User.objects.get(username=request.user.username)
        obj.nguoi_kiem_tra_minh_chung = u
        if obj.trang_thai == "Đã xử lý":
            print(obj.trang_thai)
            obj.hoat_dong.user_svs.add(obj.sinh_vien)
        return super(SinhVienMinhChungAdmin, self).save_model(request, obj, form, change)

    def has_module_permission(self, request):
        return True


class LopAdmin(admin.ModelAdmin):
    list_display = [l.name for l in Lop._meta.fields]
    list_filter = ['id', 'name']
    search_fields = ['name']

    def has_module_permission(self, request):
        return True


class KhoaAdmin(admin.ModelAdmin):
    list_display = [k.name for k in Khoa._meta.fields]
    list_filter = ['id', 'name']
    search_fields = ['name']

    def has_module_permission(self, request):
        return True


class QuyCheAdmin(admin.ModelAdmin):
    list_display = [qc.name for qc in QuyChe._meta.fields]
    list_filter = ['id', 'name']
    search_fields = ['name']

    def has_module_permission(self, request):
        return True


class HocKiAdmin(admin.ModelAdmin):
    list_display = [qc.name for qc in HocKi._meta.fields]
    list_filter = ['id', 'name']
    search_fields = ['name']

    def has_module_permission(self, request):
        return True


class UserAdmin(admin.ModelAdmin):
    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
        return ' '.join(groups)

    group.short_description = 'Groups'
    list_display = ['id', 'first_name', 'last_name', 'username', 'email', 'phone', 'group']
    list_filter = ['id', 'first_name', 'username', 'email']
    search_fields = ['first_name', 'username', 'email']

    def has_module_permission(self, request):
        return True

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     form.base_fields["last_login"].widget = forms.HiddenInput()
    #     form.base_fields["user_permissions"].widget = forms.HiddenInput()
    #     form.base_fields["is_superuser"].widget = forms.HiddenInput()
    #     form.base_fields["is_staff"].widget = forms.HiddenInput()
    #     form.base_fields["date_joined"].widget = forms.HiddenInput()
    #     return form

    # def save_model(self, request, obj, form, change):
    #     print(obj.password)
    #     obj.password = obj.set_password(obj.password)
    #     obj.save()
    #     super().save_model(request, obj, form, change)


class UserSVAdmin(admin.ModelAdmin):
    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
        return ' '.join(groups)

    group.short_description = 'Groups'
    list_display = ['id', 'mssv', 'first_name', 'last_name', 'username', 'email', 'phone', 'group']
    list_filter = ['id', 'first_name', 'username', 'email', 'mssv']
    search_fields = ['first_name', 'username', 'email', 'mssv']
    readonly_fields = ('MSSV', )

    def has_module_permission(self, request):
        return True

    def MSSV(self, obj):
        return f'{(UserSV.objects.all().count()+1):010}'

    def get_readonly_fields(self, request, obj=None):
        path = request.path
        path_tmp = ""
        if obj is not None:
            path_tmp = f'/admin/DRL/usersv/{obj.id}/change/'
        if path == path_tmp:
            self.readonly_fields = ('mssv',)
        else:
            self.readonly_fields = ('MSSV',)
        return self.readonly_fields

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        path = request.path
        # path_tmp = ""
        # if obj is not None:
        #     path_tmp = f'/admin/DRL/usersv/{obj.id}/change/'
        # if path == path_tmp:

        if path == '/admin/DRL/usersv/add/':
            form.base_fields["mssv"].widget = forms.HiddenInput()
        return form


admin_site = DRLAppAdminSite(name="myapp")

admin_site.register(HoatDong,HoatDongAdmin)
admin_site.register(Lop, LopAdmin)
admin_site.register(Khoa, LopAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(UserSV, UserSVAdmin)
admin_site.register(Permission)
admin_site.register(Tag)
admin_site.register(Comment)
admin_site.register(Like)
admin_site.register(SinhVienMinhChungHoatDong, SinhVienMinhChungAdmin)
admin_site.register(ThanhTichNgoaiKhoa)
admin_site.register(QuyChe, QuyCheAdmin)
admin_site.register(HocKi, HocKiAdmin)
admin_site.register(Group)




