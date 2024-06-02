from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("register", views.register, name='register'),
    path("dashboard", views.dashboard, name='dashboard'),
    path("account", views.account, name='account'),
    path("property-create", views.property_create, name="property-create"),
    path("logout", views.logout, name='logout'),
    path("login", views.login, name='login'),
]
