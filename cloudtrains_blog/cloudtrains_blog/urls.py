"""cloudtrains_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

# re_path()
from django.contrib.sitemaps.views import sitemap
# from .blog import sitemaps
from blog.feed import LatestPostsFeed
from blog.sitemap import PostSiteMap

sitemaps = {
    'posts': PostSiteMap
}
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', auth_views.LoginView),
    path('blog/', include('blog.urls', namespace='blog')),
    # path(r'', include('django_blog_it.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
    name='django.contrib.sitemaps.views.sitemap'),
    path('feed/', LatestPostsFeed(), name='post_feed'),

]
