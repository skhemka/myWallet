from django.conf.urls import patterns, url

from wallet import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<style>\d+)/$', views.detail, name='detail'),
)

