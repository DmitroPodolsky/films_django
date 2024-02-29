from dataclasses import asdict

import pytest
from rest_framework.test import APIClient

from films.models import Actor
from films.models import Director
from films.models import Movie
from films.tests.client_data import create_movie_data
from films.tests.conftest import client
from films.tests.schemas import DirectorData


# positive case
@pytest.mark.django_db
def test_create_movie(client: APIClient) -> None:
    """
    Test creating a member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """
    actor = Actor.objects.create(name="laaaa")
    director = Director.objects.create(name="laaaa")
    response = client.post(
        "/api/movies/",
        {
            "title": "director",
            "director": {"name": director.name},
            "actors": [{"name": actor.name}],
            "release_year": "1199-04-23",
        },
        format="json",
    )
    assert response.status_code == 201
    assert Movie.objects.filter(title="director").exists()


@pytest.mark.django_db
def test_create_movie_missing_required_fields(client: client) -> None:
    """
    Test creating a member with missing required fields via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """
    response = client.post("/api/movies/", data={"some_field": "some_value"})
    assert response.status_code == 400
    assert not Movie.objects.exists()
