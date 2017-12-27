from django.conf.urls import url
from .views import post_list, post_detail, category_detail

urlpatterns = [
    url(r'^post-list/$', post_list, name='post_list'),
    url(r'^post-detail/(?P<slug>[-\w]+)/$', post_detail, name='post_detail'),
    url(r'^category-detail/(?P<slug>[-\w]+)/$', category_detail, name='category_detail'),
]
