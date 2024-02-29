import pytest
from rest_framework.test import APIClient

from films.models import Actor
from films.models import Director
from films.models import Movie


@pytest.mark.django_db
def test_delete_movie(client: APIClient) -> None:
    """
    Test deleting a member via API.

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

    response = client.delete(f"/api/movies/{movie.id}/")
    assert response.status_code == 204
    assert not Director.objects.filter(id=movie.id).exists()


@pytest.mark.django_db
def test_delete_nonexistent_movie(client: APIClient) -> None:
    """
    Test deleting a nonexistent member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
    """
    response = client.delete("/api/movies/999/")
    assert response.status_code == 404
