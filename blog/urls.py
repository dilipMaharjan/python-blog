from django.conf.urls import url
from .views import PostListView, PostDetailView, post_list, post_detail

urlpatterns = [
    url(r'^blog-list/$', PostListView.as_view(), name='list'),
    url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^blog-f-detail/$', post_list, name='list'),
    url(r'^(?P<slug>[-\w]+)/$', post_detail, name='detail'),
]
