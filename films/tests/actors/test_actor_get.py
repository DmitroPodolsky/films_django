import pytest
from rest_framework.test import APIClient

from films.models import Actor


@pytest.mark.django_db
def test_get_actors(client: APIClient) -> None:
    """
    Test retrieving list of members via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
    """
    Actor.objects.create(name="laaaa")
    Actor.objects.create(name="muu")

    response = client.get(f"/api/actors/")
    assert response.status_code == 200
    assert response.data["count"] == Actor.objects.count()


@pytest.mark.django_db
def test_get_actor(client: APIClient) -> None:
    """
    Test retrieving a specific member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """
    actor = Actor.objects.create(name="laaaa")

    response = client.get(f"/api/actors/{actor.id}/")
    assert response.status_code == 200
    assert response.data["name"] == Actor.objects.get(id=actor.id).name


@pytest.mark.django_db
def test_get_nonexistent_actor(client: APIClient) -> None:
    """
    Test retrieving details of a nonexistent member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
    """
    response = client.get("/api/actors/999/")
    assert response.status_code == 404
