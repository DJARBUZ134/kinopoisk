from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path(
        'movie_detail/<int:movie_id>/',
        movie_detail, name='movie_detail' 
    ),
    path(
        'actor_detail/<int:actor_id>/',
        actor_detail, name='actor_detail' 
    ),
    path(
        'director_detail/<int:director_id>/',
        director_detail, name='director_detail' 
    ),
    path(
        'sound_enginner_detail/<int:sound_enginner_id>/',
        sound_engineer_detail, name='sound_engineer_detail' 
    ),
    path(
        'genre_detail/<int:movie_id>/',
        genre_detail, name='genre_detail' 
    ),
    path('movie_list/', movie_list, name='movie_list' ),
    path('director_list/', directors_list, name='director_list' ),
    path('genre_list/', genres_list, name='genre_list' ),
    path('actor_list/', actor_list, name='actor_list' ),
    path('sound_engineer_list/', sound_engineer_list, name='sound_engineer_list' ),
]