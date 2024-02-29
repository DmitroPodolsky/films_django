from django.urls import path

from .views import ActorDetail
from .views import ActorList
from .views import DirectorDetail
from .views import DirectorList
from .views import MovieDetail
from .views import MovieList

urlpatterns = [
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actor-detail"),
    path("directors/", DirectorList.as_view(), name="director-list"),
    path("directors/<int:pk>/", DirectorDetail.as_view(), name="director-detail"),
    path("movies/", MovieList.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieDetail.as_view(), name="movie-detail"),
]
