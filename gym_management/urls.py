"""
URL configuration for gym_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path
from gym import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("add-member/", views.add_member, name="add_member"),
    path("member/", views.member_list, name="member_list"),
    path("update-member/<int:id>/", views.update_member, name="update_member"),
    path("delete-member/<int:id>/", views.delete_member, name="delete_member"),
    path("add-trainer/", views.add_trainer, name="add_trainer"),
    path("trainers/", views.trainer_list, name="trainer_list"),
    path("delete-trainer/<int:id>/", views.delete_trainer, name="delete_trainer"),
    path("add-attendance/", views.add_attendance, name="add_attendance"),
    path("attendance-list/", views.attendance_list, name="attendance_list"),
    path("add-payment/", views.add_payment, name="add_payment"),
    path("payment-list/", views.payment_list, name="payment_list"),
]
