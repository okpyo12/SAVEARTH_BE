from .serializers import UserSerializer, LoginSerializer
from django.contrib.auth import login, logout
from .models import User
from rest_framework import views, status, permissions, generics, authentication
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# 회원가입
class UserCreate(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 로그인
class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=self.request.data,context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token = Token.objects.get(user=user)
        return Response({"Token": token.key}, status=status.HTTP_202_ACCEPTED)
    
    def get(self, reqeust):
        return Response(None, status=status.HTTP_202_ACCEPTED)

# 로그아웃
class LogoutView(views.APIView):

    def post(self, request, format=None):
        logout(request)
        return Response(None, status=status.HTTP_202_ACCEPTED)
    
    def get(self, reqeust):
        return Response(None, status=status.HTTP_202_ACCEPTED)

# 유저 정보
class UserView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    
    def get(self, request, format=None):
        usernames = request.user.nickname
        queryset = User.objects.filter(nickname=usernames)
        return Response(queryset.values())