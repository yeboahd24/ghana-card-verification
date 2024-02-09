# urls.py
from django.urls import path
from .views import VerifyUserAPIView

urlpatterns = [
    path("verify/", VerifyUserAPIView.as_view(), name="api_verify_user"),
]
