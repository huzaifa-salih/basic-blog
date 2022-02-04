# from turtle import pos
from dataclasses import field
from django.shortcuts import render
from post.models import Post
from post.forms import PostForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView


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


class PostList(ListView):
    model = Post


class PostDetail(DetailView):
    model = Post


class PostUpdate(UpdateView):
    model = Post
    fields = ["title", "content", "created_at"]
    template_name = "post_edit.html"
    success_url = "/blog/cbv"


class PostCreate(CreateView):
    model = Post
    fields = ["title", "content", "created_at", "puplished_at", "email", "views_count"]
    template_name = "create_post.html"
    success_url = "/blog/cbv"