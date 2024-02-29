import pytest
from rest_framework.test import APIClient

from films.models import Actor
from films.models import Director
from films.models import Movie


@pytest.mark.django_db
def test_get_movies(client: APIClient) -> None:
    """
    Test retrieving list of members via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
    """
    director = Director.objects.create(name="laaaa")
    actor = Actor.objects.create(name="laaaa")
    movie = Movie.objects.create(
        title="laaaa", director=director, release_year="1994-04-23"
    )
    movie.actors.set([actor])
    movie = Movie.objects.create(
        title="laaaa", director=director, release_year="1994-04-23"
    )
    movie.actors.set([actor])

    response = client.get("/api/movies/")
    assert response.status_code == 200
    assert response.data["count"] == Movie.objects.count()


@pytest.mark.django_db
def test_get_movie(client: APIClient) -> None:
    """
    Test retrieving a specific member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """
    director = Director.objects.create(name="laaaa")
    actor = Actor.objects.create(name="laaaa")
    movie = Movie.objects.create(
        title="laaaa", director=director, release_year="1994-04-23"
    )
    movie.actors.set([actor])

    response = client.get(f"/api/movies/{movie.id}/")
    assert response.status_code == 200
    assert response.data["title"] == Movie.objects.get(id=movie.id).title


@pytest.mark.django_db
def test_get_nonexistent_movie(client: APIClient) -> None:
    """
    Test retrieving details of a nonexistent member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
    """
    response = client.get("/api/movies/999/")
    assert response.status_code == 404
