from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dbcheck$', views.dbcheck_main, name='dbcheck_main'),
    url(r'^dbcheck/(?P<pk>\d+)/$', views.instdetail, name='instdetail'),
]