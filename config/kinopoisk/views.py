from django.shortcuts import render
from .models import *

# Create your views here.
def main(request):
    movie = Movie.objects.all()
    return render(request, 'kinopoisk/main.html' , {'movies': movie})


def actor_detail(request, actor_id):
    actor = Movie.objects.get(id=actor_id)
    movies = actor.acted_in_movies.all()
    return render(request, 'kinopoisk/actor_detail.html', {
        'person': actor, 'movies':movies
        })

def director_detail(request, director_id):
    director = Movie.object.get(id=director_id)
    movies = director.directed_movies.all()
    return render(request, 'kinopoisk/director_detail.html', {
        'person': director, 'movies':movies
        })

def directors_list(request):
    directors = MoviePerson.object.filter(role = MoviePerson.RoleType.DIRECTOR)
    return render(request, 'kinopoisk/director_list.html', {
        'persons': directors, 'title': 'Директора'
    } )

def genres_list(request):
    genres = Movie.objectAll()
    return render(request, 'kinopoisk/genre_list.html', {'genres': genres} )

def genre_detail(request, genre_id):
    genre = Movie.objects.get(id=genre_id)
    movies = Movie.objects.all()
    return render(request, 'kinopoisk/genre_detail.html', {
        'genre': genre, 'movies':movies
        })

def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'kinopoisk/movie_detail.html', {'movies': movie})

def movie_list(request):
    movie = Movie.objectAll()
    return render(request, 'kinopoisk/movie_list.html' , {'movies': movie})

def actor_list(request):
    actor = MoviePerson.objects.filter(role=MoviePerson.RoleType.ACTOR)
    return render(request, 'kinopoisk/actors_list.html', {
        'persons': actor, 'title': 'Актеры'
    } )

def sound_engineer_detail(request, sound_engineer_id):
    sound_engineer = Movie.object.get(id=sound_enginner_id)
    movies = sound_engineer.sounded_movies.all()
    return render(request, 'kinopoisk/sound_engineer_detail.html', {
        'person': sound_engineer, 'movies': movies
        })

def sound_engineer_list(request):
    actor = MoviePerson.object.filter(role = MoviePerson.RoleType.SOUND_ENGINEER)
    movies = actor.acted_in_movies.all()
    return render(request, 'kinopoisk/sound_enginner_list.html', {
        'persons': sound_engineers , 'title': 'Звукорежиссёры'
    } )