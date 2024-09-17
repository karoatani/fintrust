from rest_framework import generics
from .models import Account
from .serializers import SignupSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password

class SignupAPIView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       serializer.validated_data["password"] = make_password(serializer.validated_data["password"])
       self.perform_create(serializer)
       headers = self.get_success_headers(serializer.data)
       return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class SigninAPIView(TokenObtainPairView):
    pass

class SigninRefreshAPIView(TokenRefreshView):
    pass