from django.urls import path, include
from . import views

urlpatterns = [
    path("login-user/", views.login_user, name="login_user")
]
