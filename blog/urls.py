from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog$', views.post_list, name='post_list'),
    url(r'^post/(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]