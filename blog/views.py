from django.shortcuts import render, get_object_or_404

from .models import Post, Category
from .forms import PostForm
from django.contrib import messages
from .utils import pagination

# function based list view
def post_list(request):
    template = 'post/post_list.html'

    object_list = Post.objects.filter(status='Published').order_by('id')
    
    pages = pagination(request, object_list, num=3)

    context = {
    'items': pages[0],
    'page_range': pages[1]
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
    try:
        if post.is_valid():
            post.save()
            messages.success(request,"Post saved successfully.")
    except Exception as e:
         messages.warning(request,"Post couldn't be saved successfully.Error :{}".format(e))
    context = {
        'form':post,
    }
    return render(request,template,context)

def post_list_admin(request):
    template = 'post/post_list_admin.html'
    post = Post.objects.all()
    pages = pagination(request, post, num=3)
    context = {
    'items': pages[0],
    'page_range': pages[1]
    }

    return render(request, template, context)

def edit_post(request, pk):
    template = 'post/new_post.html'
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, "Your Blog Post Was Successfully Updated")

        except Exception as e:
            messages.warning(request, 'Your Post Was Not Saved Due To An Error: {}'.format(e))

    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }
    return render(request, template, context)