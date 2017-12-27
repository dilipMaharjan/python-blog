from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Post, Category


# class based list view
class PostListView(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['object_list'] = Post.objects.filter(status='Published')
        return context


# class based detail view
class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        return context


# function based list view
def post_list(request):
    template = 'blog/post_list.html'
    objects_list = Post.objects.filter(status='Published')
    context = {
        'objects_list': objects_list,
    }
    return render(request, template, context)


# function based list view
def post_detail(request, slug):
    template = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post,
    }
    return render(request, template, context)


# function based list view
def category_detail(request, slug):
    template = 'category/category_detail.html'

    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category)
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, template, context)
