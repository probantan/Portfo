from django.conf.urls import url
from django.conf import settings
from . import views


urlpatterns=[
    url('^$', views.home_page, name='home'),
    url(r'^About/$', views.About_page, name='About'),

]