from turtle import pos
from django.shortcuts import render
from post.models import Post
from post.forms import PostForm


def post_list(request):
    all_post = Post.objects.all()
    context = {
        "all_post": all_post,
    }
    return render(request, "post_list.html", context)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        "post": post,
    }
    return render(request, "post_detail.html", context)


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    context = {
        "form": form,
    }
    return render(request, "create_post.html", context)


def post_edit(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
    else:
        form = PostForm(instance=post)
    context = {
        "form": form,
        # "post": post,
    }
    return render(request, "post_edit.html", context)
