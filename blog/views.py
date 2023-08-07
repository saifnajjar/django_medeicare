from itertools import groupby
from operator import itemgetter
from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all().order_by('-date_posted')
    grouped_posts = []
    for key, group in groupby(posts, key=lambda x: x.category):
        grouped_posts.append({
            'category': key,
            'posts': list(group)[:3],  # عرض أحدث ثلاثة منشورات فقط
        })
    context = {
        'grouped_posts': grouped_posts
    }
    return render(request, 'BLOG/BLOG_LIST.html', context)


from django.shortcuts import render, get_object_or_404
from .models import Post

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post).order_by('-date_posted')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'BLOG/SINGLE_POST.html', context)









    



