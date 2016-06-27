from django.contrib import admin
from .models import Genres
from .models import Tracks

admin.site.register(Genres)
admin.site.register(Tracks)
