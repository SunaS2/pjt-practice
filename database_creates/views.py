from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import GenreSerialzier
import requests
import pandas as pd

# TMDB API 키 설정
API_KEY = "76579a872d47b39b4c1aae95895e2a3e"

# TMDB API URL 설정
BASE_URL = "https://api.themoviedb.org/3"
MOVIE_LIST_URL = f"{BASE_URL}/movie/popular"
GENRE_LIST_URL = f'{BASE_URL}/genre/movie/list'

# Create your views here.
@api_view(['GET'])
def get_genre(request):
    params = {
        "api_key": API_KEY,
    }
    result = None
    response = requests.get(GENRE_LIST_URL, params=params)
    if response.status_code == 200:
        result = response.json()
    else:
        print(f"Error: {response.status_code}")
    
    for genre in result["genres"]:
        data ={
            "tmdb_id": genre["id"],
            "name": genre["name"]
        }
        serializer = GenreSerialzier(data=data)
        if serializer.is_valid():
            serializer.save()
    