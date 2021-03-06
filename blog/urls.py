"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path

from blog import views_cbv
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views_cbv.post_list, name='post_list'),
    # re_path(r'^(?P<id>\d+)/$', views.post_detail),
    path('<int:pk>/', views_cbv.post_detail, name='post_detail'),
    path('new', views.post_new, name='post_new'),
    path('<int:id>/edit/', views.post_edit, name = "post_edit"),
    path('cbv/new/', views_cbv.post_new),
    path('cbv/<int:pk>/edit/', views_cbv.post_edit),
    path('cbv/<int:pk>/delete/', views_cbv.post_delete),

]
