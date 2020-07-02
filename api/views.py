from django.contrib.auth.models import Group, Permission
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework import settings
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle

from api.authentications import MyAuth
from api.permissions import MyPermission
from api.throttle import SendMessageRate
from api.models import User
from utils.response import APIResponse


class TestAPIView(APIView):
    authentication_classes = [MyAuth]

    def get(self, request, *args, **kwargs):
        # 查询用户
        user = User.objects.first()
        # 获取对应的角色
        print(user.groups.first())
        # 获取对应的权限
        print(user.user_permissions.first().name)

        return APIResponse("OK")


class TestPermissionAPIView(APIView):
    authentication_classes = [MyAuth]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return APIResponse("登录访问成功")


class UserLoginOrReadOnly(APIView):
    throttle_classes = [UserRateThrottle]

    # permission_classes = [MyPermission]

    def get(self, request, *args, **kwargs):
        return APIResponse("读操作访问成功")

    def post(self, request, *args, **kwargs):
        return APIResponse("写操作")


class SendMessageAPIView(APIView):
    throttle_classes = [SendMessageRate]

    def get(self, request, *args, **kwargs):
        return APIResponse("读操作访问成功")

    def post(self, request, *args, **kwargs):
        return APIResponse("写操作")
