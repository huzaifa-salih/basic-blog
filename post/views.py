from django.shortcuts import render
from post.models import Post

def post_list(request):
    all_posts = Post.objects.all()

    return render(request, "post_list.html", {"all_posts": all_posts})


def post_detail(request, id):
    post = Post.objects.get(id=id)

    return render(request, "post_detail.html", {"post": post})
