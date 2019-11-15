from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'active',)
    list_filter = ('active',)
    search_fields = ('name',)
    ordering = ('id',)


admin.site.register(Movie, MovieAdmin)
