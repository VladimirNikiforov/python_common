"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin

from post.views import (
	bookshome,
	bookscreate,
	booksdetail,
	booksupdate,
	booksdelete,
	bookslist,
)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
#	url(r'^posts/$', "post.views.posthome")
#	url(r'^posts/$', views.posthome)
#	url(r'^create/$', "post.views.postcreate"),
#	url(r'^detail/$', "post.views.postdetail"),
#	url(r'^list/$', "post.views.postlist"),
#	url(r'^update/$', "post.views.postupdate"),
#	url(r'^delete/$', "post.views.postdelete"),
	url(r'create/$', bookscreate),
	#url(r'^detail/$', booksdetail),
	url(r'(?P<id>\d+)/$', booksdetail),
	url(r'list/$', bookslist),
	url(r'update/$', booksupdate),
	url(r'delete/$', booksdelete),
	
	url(r'books/$', bookshome),
	url(r'$', bookslist),
]
