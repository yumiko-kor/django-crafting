from django.shortcuts import render, redirect
from .models import Post

# main
def index(request):
    return render(request,'main/index.html')

def board(request):
    postlist = Post.objects.all()
    
    return render(request, 'main/board.html', {'postlist': postlist})

def posting(request, pk):
    # pk를 통하여 게시글을 탐색
    post = Post.objects.get(pk=pk)
    
    # 템플릿에 게시글 객체를 post라는 이름으로 전달하여 렌더링
    return render(request, 'main/posting.html', {'post': post})

def post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            new_article=Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/board/')
    return render(request, 'main/post.html')

def remove(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/board/')
    return render(request, 'main/remove.html', {'post': post})