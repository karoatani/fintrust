from .views import SignupAPIView, SigninAPIView, SigninRefreshAPIView
from django.urls import path


urlpatterns = [
    path("sign-up/", SignupAPIView.as_view(), name="sign-up"),
    path("sign-in/", SigninAPIView.as_view(), name="sign-in" ),
    path("sign-in/refresh/",SigninRefreshAPIView.as_view(), name="sigin-refresh")
]