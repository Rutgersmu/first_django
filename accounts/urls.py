from django.urls import path, re_path

from accounts import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile),
]