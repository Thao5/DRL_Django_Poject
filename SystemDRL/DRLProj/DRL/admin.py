from django.contrib import admin
from django import forms
from django.template.response import TemplateResponse
from django.urls import path
from django.utils.html import mark_safe
from django.contrib.auth.models import Permission, Group
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import HoatDong, Tag, Lop, Khoa, User, UserSV, QuyChe, ThanhTichNgoaiKhoa, Comment, Like, SinhVienMinhChungHoatDong, HocKi
from .dao import order_drl_by_khoa


# Register your models here.


class DRLAppAdminSite(admin.AdminSite):
    site_header = "TRANG QUẢN TRỊ HỆ THỐNG ĐÁNG GIÁ ĐIỂM RÈN LUYỆN"
    index_title = "TRANG QUẢN TRỊ HỆ THỐNG ĐÁNG GIÁ ĐIỂM RÈN LUYỆN"

    def get_urls(self):
        return [
                   path('drl-stats/', self.stats_view)
               ] + super().get_urls()

    def stats_view(self, request):
        stats = order_drl_by_khoa(request.GET)
        khoas = Khoa.objects.all()
        lops = Lop.objects.all()
        return TemplateResponse(request, 'admin/stats_view.html',{
            'stats': stats,
            'site_header': DRLAppAdminSite.site_header,
            'index_title': 'STATS',
            'khoas': khoas,
            'lops': lops
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


class LopAdmin(admin.ModelAdmin):
    list_display = [l.name for l in Lop._meta.fields]
    list_filter = ['id', 'name']
    search_fields = ['name']


class KhoaAdmin(admin.ModelAdmin):
    list_display = [k.name for k in Khoa._meta.fields]
    list_filter = ['id', 'name']
    search_fields = ['name']


class QuyCheAdmin(admin.ModelAdmin):
    list_display = [qc.name for qc in QuyChe._meta.fields]
    list_filter = ['id', 'name']
    search_fields = ['name']


class HocKiAdmin(admin.ModelAdmin):
    list_display = [qc.name for qc in HocKi._meta.fields]
    list_filter = ['id', 'name']
    search_fields = ['name']


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
    readonly_fields = ['avatar']

    def img(self, obj):
        if obj:
            return mark_safe(
                '<img src="/static/{url}" width="120" />'\
                    .format(url=obj.image.name)
            )

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

    def MSSV(self, obj):
        return f'{(UserSV.objects.all().count()+1):010}'

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
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
admin_site.register(SinhVienMinhChungHoatDong)
admin_site.register(ThanhTichNgoaiKhoa)
admin_site.register(QuyChe, QuyCheAdmin)
admin_site.register(HocKi, HocKiAdmin)
admin_site.register(Group)




