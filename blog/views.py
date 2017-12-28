from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, Category
from .forms import PostForm

# function based list view
def post_list(request):
    template = 'post/post_list.html'
    objects_list = Post.objects.filter(status='Published').order_by('id')
    paginator = Paginator(objects_list, 2)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)
    context = {
        'items': items,
    }
    return render(request, template, context)


# function based list view
def post_detail(request, slug):
    template = 'post/post_detail.html'
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

def new_post(request):
    template='post/new_post.html'

    post=PostForm(request.POST or None)

    if post.is_valid():
        post.save()
    else:
        post=PostForm()

    context = {
        'form':post,
    }
    return render(request,template,context)