from django.urls import path, re_path

from accounts import views

urlpatterns = [
    path('profile/', views.profile)
]