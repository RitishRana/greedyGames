import json
import os

from django.conf import settings
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .models import *


# Create your views here.

def all_tracks(request):
    all_tracks_avail = Tracks.objects.values_list('track_title', 'id')
    tracks = map(lambda x: {'track_name': str(x[0]), 'id': x[1]}, all_tracks_avail)
    context = {
        "tracks": tracks
    }
    return JsonResponse(context)


def track_details(request, track_id):
    track = Tracks.objects.get(id=track_id)
    context = {
        "rating": track.track_rating,
        "title": track.track_title,
        "genre_name": track.track_genre.genre_name
    }
    return JsonResponse(context)


def all_genres(request):
    genres = Genres.objects.all()
    json_serializer = serializers.get_serializer("json")
    json_data = json_serializer()
    json_data.serialize(genres)
    data = json_data.getvalue()
    return HttpResponse(data)


def genre_details(request, genre_id):
    return None


def home(req):
    return render(req, 'main.html', {'STATIC_URL': os.path.join(settings.BASE_DIR, 'tracks') + settings.STATIC_URL})


def genre_edit(request, new_name, id):
    genre = Genres.objects.get(pk=id)
    genre.genre_name = new_name
    genre.save()
    return HttpResponse("Done")


def genre_add(request, new_genre_name):
    new_genre = Genres(genre_name=new_genre_name)
    new_genre.save()
    return HttpResponse("Added")


def track_add(request):
    if request.method == "POST":
        form = json.loads(request.body)
        new_track = Tracks(track_title=form['title'], track_rating=form['rating'], track_genre_id=form['genre_id'])
        new_track.save()

    return HttpResponse("Added")


def track_search(request, track_search_pattern):
    track_title = list(Tracks.objects.filter(track_title__contains=str(track_search_pattern)))
    tracks_all = Tracks.objects.all()
    track_genre = filter(lambda x: track_search_pattern in str(x.track_genre.genre_name), tracks_all)
    result = set(track_title + track_genre)
    result = list(result)

    tracks = map(lambda x: {'track_name': str(x.track_title), 'id': x.id}, result)
    context = {
        "tracks": tracks
    }
    return JsonResponse(context)
