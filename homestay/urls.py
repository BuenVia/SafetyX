from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("register", views.register, name='register'),
    path("dashboard", views.dashboard, name='dashboard'),
    path("account", views.account, name='account'),
    path("property-create", views.property_create, name="property-create"),
    path("property-edit/<id>", views.property_edit, name="property-edit"),
    path("property-edit/delete/<id>", views.property_delete, name="property-delete"),
    path("business-create", views.business_create, name="business-create"),
    path("question/<id>", views.question_set, name="question_set"),
    path("logout", views.logout, name='logout'),
    path("login", views.login, name='login'),
]
