from django.contrib import admin
from movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    listDisplay = ('id', 'title', 'genre', 'release_date', 'actors', 'resume')
