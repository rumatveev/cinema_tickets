from django.contrib import admin
from .models import Movie, Showing


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'active',)
    list_filter = ('active',)
    search_fields = ('name',)
    ordering = ('id',)


admin.site.register(Movie, MovieAdmin)


class ShowingAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_ticket', 'movie', 'showing_room', 'remaining_seats',
                    'start', 'end', 'status')
    list_filter = ('movie', 'showing_room', 'status')
    search_fields = ('movie',)
    ordering = ('id',)


admin.site.register(Showing, ShowingAdmin)