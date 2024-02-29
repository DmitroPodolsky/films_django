from dataclasses import asdict

import pytest
from rest_framework.test import APIClient

from films.models import Actor
from films.models import Director
from films.models import Movie
from films.tests.client_data import create_movie_data
from films.tests.schemas import DirectorData


@pytest.mark.django_db
def test_update_movie(client: APIClient) -> None:
    """
    Test updating a member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """
    director = Director.objects.create(name="laaaa1")
    actor = Actor.objects.create(name="laaaa")
    movie = Movie.objects.create(
        title="laaaa", director=director, release_year="1994-04-23"
    )
    movie.actors.set([actor])

    response = client.patch(
        f"/api/movies/{movie.id}/", {"title": "director"}, format="json"
    )
    assert response.status_code == 200
    assert Movie.objects.get(id=movie.id).title == "director"


@pytest.mark.django_db
def test_update_nonexistent_movie(client: APIClient) -> None:
    """
    Test updating a nonexistent member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """
    response = client.put("/api/movies/999/", data={"name": "some_name"})
    assert response.status_code == 404


@pytest.mark.django_db
def test_update_missingfields_movie(client: APIClient) -> None:
    """
    Test updating a nonexistent member via API.

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

    response = client.put(f"/api/movies/{movie.id}/", data={"some_field": "some_field"})
    assert response.status_code == 400
