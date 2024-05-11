from django.contrib.auth.models import Group

from .models import HoatDong, Tag, Lop, Khoa, User, UserSV, QuyChe, ThanhTichNgoaiKhoa, Comment, Like, \
    SinhVienMinhChungHoatDong, HocKi
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from DRLProj import settings


class LopSerializer(ModelSerializer):
    class Meta:
        model = Lop
        fields = '__all__'


class KhoaSerializer(ModelSerializer):
    class Meta:
        model = Khoa
        fields = '__all__'


class QuyCheSerializer(ModelSerializer):
    class Meta:
        model = QuyChe
        fields = '__all__'


class HocKiSerializer(ModelSerializer):
    class Meta:
        model = HocKi
        fields = '__all__'


class ThanhTichNgoaiKhoaSerializer(ModelSerializer):
    class Meta:
        model = ThanhTichNgoaiKhoa
        fields = ['id', 'diem', 'thanh_tich']


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'is_like']


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class MinhChungSerializer(ModelSerializer):
    minh_chung = serializers.SerializerMethodField(source='minh_chung')

    def get_minh_chung(self, obj):
        request = self.context.get('request')
        if obj.minh_chung:
            if request:
                return request.build_absolute_uri("/static/minh_chung/%s" % obj.minh_chung.name)
            return "/%s" % obj.minh_chung.name

    def create(self, validated_data):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
        data = validated_data.copy()
        mc = SinhVienMinhChungHoatDong(**data)
        u = UserSerializer(user).data
        sv = UserSV.objects.get(username=u.get('username'))
        mc.minh_chung = request.FILES.get('minh_chung')
        mc.sinh_vien_id = sv.id
        mc.trang_thai = "Đang xử lý"
        mc.save()

        return mc

    class Meta:
        model = SinhVienMinhChungHoatDong
        fields = ['minh_chung', 'trang_thai', 'hoat_dong', 'sinh_vien', 'nguoi_kiem_tra_minh_chung']
        extra_kwargs = {
            'trang_thai': {
                'read_only': True
            },
            'sinh_vien': {
                'read_only': True
            }
        }


class BaseSerializer(ModelSerializer):
    image = serializers.SerializerMethodField(source='image')
    tags = TagSerializer(many=True)

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            if request:
                return request.build_absolute_uri("/static/%s" % obj.image.name)
            return "/%s" % obj.image.name


class UserSVSerializer(ModelSerializer):
    avatar_path = serializers.SerializerMethodField(source='avatar')
    # hoat_dongs = HoatDongSerializer(many=True)
    khoa = KhoaSerializer(read_only=True)
    khoa_id = serializers.IntegerField(
        write_only=True
    )
    lop = LopSerializer(read_only=True)
    lop_id = serializers.IntegerField(
        write_only=True
    )

    class Meta:
        model = UserSV
        ref_name = "User SV"
        exclude = ('is_superuser', 'is_staff', 'last_login', 'is_active', 'user_permissions', 'groups', 'date_joined',)
        extra_kwargs = {
            'password': {
                'write_only': True
            },
            'mssv': {
                'read_only': True
            },
            'username':{
                'read_only': True
            }
        }

    def create(self, validated_data):
        nhom = Group.objects.get(name='SV')
        data = validated_data.copy()
        # hds_data = data.pop('hoat_dongs', [])
        # ids = [hd.get('id') for hd in hds_data if hd]
        # h = HoatDong.objects.filter(id__in=ids)
        user = UserSV(**data)
        user.username = user.email
        # user.hoat_dongs.add(*h)
        user.save()
        user.groups.add(nhom)
        user.save()

        return user

    def get_avatar_path(self, obj):
        request = self.context.get('request')
        print('ava')
        if obj.avatar:
            if request:
                return f"{settings.CLOUDINARY_URL}{obj.avatar}"
            return f"{settings.CLOUDINARY_URL}{obj.avatar}"


class HoatDongSerializer(ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True
    )
    user_svs = UserSVSerializer(many=True, required=False, read_only=True)
    user_sv_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True
    )
    # tags = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=Tag.objects.all(),
    #     default=[]
    # )
    # user_svs = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=UserSV.objects.all(),
    #     default=[]
    # )

    # user_svs = serializers.HyperlinkedRelatedField(many=True, read_only=False, view_name='hd-sv',
    #                                              queryset=UserSV.objects.all())

    class Meta:
        model = HoatDong
        fields = ['id', 'name', 'mo_ta', 'ngay_du_kien', 'ngay_dien_ra', 'ngay_het', 'diem_cong', 'quy_che', 'tags',
                  'user_svs', 'tag_ids', 'user_sv_ids']

    def create(self, validated_data):
        data = validated_data.copy()
        tag_ids = validated_data.pop('tag_ids')
        user_sv_ids = validated_data.pop('user_sv_ids')
        hoat_dong = HoatDong.objects.create(**validated_data)
        hoat_dong.tags.set(tag_ids)
        hoat_dong.user_svs.set(user_sv_ids)

        return hoat_dong


class UserSerializer(ModelSerializer):
    # avatar = serializers.SerializerMethodField(source='avatar')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'phone', 'avatar']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        data = validated_data.copy()
        user = User(**data)
        user.save()

        return user

    def get_avatar(self, obj):
        request = self.context.get('request')
        if obj.avatar:
            if request:
                return f"{settings.CLOUDINARY_URL}{obj.avatar}"
            return f"{settings.CLOUDINARY_URL}{obj.avatar}"


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(
        write_only=True
    )

    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'user_id']


class HoatDongSerializerDetail(HoatDongSerializer):
    # like = serializers.SerializerMethodField(source="like")
    # comment = serializers.SerializerMethodField(source="comment")
    like_set = LikeSerializer(many=True, read_only=True)
    like_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True
    )
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_ids = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True
    )

    # def __init__(self, *args, **kwargs):
    #     many = kwargs.pop('many', True)
    #     super(HoatDongSerializerDetail, self).__init__(many=many, *args, **kwargs)

    def get_like(self, hoat_dong):
        request = self.context.get('request')
        if request.user.is_authenticated:
            return hoat_dong.like_set.filter(active=True, user=request.user).exists()

    def get_comment(self, hoat_dong):
        request = self.context.get('request')
        if request.user.is_authenticated:
            return hoat_dong.like_comment.filter(active=True, user=request.user).exists()

    class Meta:
        model = HoatDongSerializer.Meta.model
        fields = HoatDongSerializer.Meta.fields + ['like_set'] + ['comment_set'] + ['like_ids'] + ['comment_ids']



