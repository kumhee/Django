from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Comment
from .forms import PostForm

# 게시물 목록을 표시
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

# 게시물 상세 내용을 표시
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # 현재 로그인한 사용자를 작성자로 설정
            post.save()
            url = reverse('board:post_list')
            return HttpResponseRedirect('/board/') 
    else:
        form = PostForm()
    return render(request, 'board/create_post.html', {'form': form})