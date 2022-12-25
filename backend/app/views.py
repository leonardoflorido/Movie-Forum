from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Movie, Review
from app.serializers import MovieSerializer, ReviewSerializer


# Create your views here.
@api_view(['GET'])
def movie_list(request, sort):
    """Get all movies in certain order"""
    if sort == 'default':
        movies = Movie.objects.all()
    else:
        movies = Movie.objects.all().order_by('-%s', sort)
    serializer = MovieSerializer(movies)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_id):
    """Get movie details"""
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['POST'])
def create_movie(request):
    """Create a movie"""
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_movie(request, movie_id):
    """Update a movie"""
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_movie(request, movie_id):
    """Delete a movie"""
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
