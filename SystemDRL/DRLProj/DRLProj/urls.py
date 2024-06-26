"""
URL configuration for DRLProj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from django.urls import path, re_path, include
from DRL.admin import admin_site
from DRL import views
import ckeditor_uploader

schema_view = get_schema_view(
    openapi.Info(
        title="DRL API",
        default_version='v1',
        description="APIs for CourseApp",
        contact=openapi.Contact(email="2051050459thao@ou.edu.vn"),
        license=openapi.License(name="Trinh Quoc Thao@2024"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('hockis', views.HocKiViewSet, basename="hockis")
router.register('lops', views.LopViewSet, basename="lops")
router.register('khoas', views.KhoaViewSet, basename="lessons")
router.register('usersvs', views.UserSVViewSet, basename="usersvs")
router.register('users', views.UserViewSet, basename="users")
router.register('comments', views.CommentViewSet, basename="comments")
router.register('likes', views.LikeViewSet, basename="likes")
router.register('tags', views.TagViewSet, basename="tags")
router.register('hoatdongs', views.HoatDongViewSet, basename="hoatdongs")
router.register('quyches', views.QuyCheViewSet, basename="quyches")
router.register('thanhtichs', views.ThanhTichViewSet, basename="thanhtichs")
router.register('minhchungs', views.MinhChungViewSet, basename="minhchungs")

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin_site.urls),
    path('o/', include('oauth2_provider.urls',
                       namespace='oauth2_provider')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),
    re_path(r'^swagger/$',
            schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$',
            schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc')
]
