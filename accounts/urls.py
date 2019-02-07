from django.conf import settings
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from accounts import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView, name='login', kwargs={'template_name': 'accounts/login_form.html'}),
    path('logout/', auth_views.LogoutView, name='logout', kwargs={'next_page': settings.LOGIN_URL}),
    path('profile/', views.profile, name='profile'),
]