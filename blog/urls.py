from django.conf.urls import url
from .views import post_list, post_detail, category_detail,new_post

urlpatterns = [
    url(r'^post-list/$', post_list, name='post_list'),
    url(r'^post-detail/(?P<slug>[-\w]+)/$', post_detail, name='post_detail'),
    url(r'^category-detail/(?P<slug>[-\w]+)/$', category_detail, name='category_detail'),
     #custom admin
    url(r'^new-post/$', new_post, name='new_post'),
]
