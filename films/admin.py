from django.contrib import admin

from .models import Actor
from .models import Director
from .models import Movie

admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Actor)
