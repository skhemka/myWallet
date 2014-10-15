from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^wallet/', include('wallet.urls', namespace="wallet")),
    url(r'^admin/', include(admin.site.urls)),
)
