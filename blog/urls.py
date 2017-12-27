from django.conf.urls import url
from .views import PostListView, PostDetailView, post_list, post_detail, category_detail

urlpatterns = [
    url(r'^post-list/$', PostListView.as_view(), name='post_list'),
    url(r'^post-detail/(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^post-f-detail/$', post_list, name='list'),
    url(r'^post-f-detail/(?P<slug>[-\w]+)/$', post_detail, name='detail'),
    url(r'^category-detail/(?P<slug>[-\w]+)/$', category_detail, name='category_detail'),
]
