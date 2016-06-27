"""greedyGames URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from tracks import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'tracks.views.home', name='home'),
    url(r'^tracks/$', views.all_tracks, name='all_tracks'),
    url(r'^track/(?P<track_id>[0-9]+)/$', views.track_details, name='track_details'),
    url(r'^track/search/(?P<track_search_pattern>[\w]+)/$', views.track_search, name='track_search'),
    url(r'^track/add/$', views.track_add, name='track_add'),

    url(r'^genres/$', views.all_genres, name='all_genres'),
    url(r'^genre/(?P<genre_id>[0-9]+)/$', views.genre_details, name='genres_details'),
    url(r'^genre/edit/(?P<new_name>[\w]+)/(?P<id>[0-9]+)$', views.genre_edit, name='genre_edit'),
    url(r'^genre/add/(?P<new_genre_name>[\w]+)/$', views.genre_add, name='genre_add'),
]




