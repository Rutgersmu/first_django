from django import forms #원래는 블로그에 폼즈 파일 따로 구현해야 하지만 설명을 위해....
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import Post

post_list = ListView.as_view(model=Post, paginate_by=10)

post_detail = DetailView.as_view(model=Post)

post_new = CreateView.as_view(model=Post)

post_edit = UpdateView.as_view(model=Post, fields='__all__')