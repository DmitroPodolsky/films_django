import pytest
from rest_framework.test import APIClient

from films.models import Actor


@pytest.mark.django_db
def test_delete_actor(client: APIClient) -> None:
    """
    Test deleting a member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """

    actor = Actor.objects.create(name="laaaa")

    response = client.delete(f"/api/actors/{actor.id}/")
    assert response.status_code == 204
    assert not Actor.objects.filter(id=actor.id).exists()


@pytest.mark.django_db
def test_delete_nonexistent_actor(client: APIClient) -> None:
    """
    Test deleting a nonexistent member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
    """
    response = client.delete("/api/actors/999/")
    assert response.status_code == 404
