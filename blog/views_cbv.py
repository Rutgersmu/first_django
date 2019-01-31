from django import forms #원래는 블로그에 폼즈 파일 따로 구현해야 하지만 설명을 위해....
from django.views.generic import CreateView
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # success_url = '/...'



post_new = PostCreateView.as_view()