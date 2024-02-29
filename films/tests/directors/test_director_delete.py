import pytest
from rest_framework.test import APIClient

from films.models import Director


@pytest.mark.django_db
def test_delete_director(client: APIClient) -> None:
    """
    Test deleting a member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """
    director = Director.objects.create(name="laaaa")

    response = client.delete(f"/api/directors/{director.id}/")
    assert response.status_code == 204
    assert not Director.objects.filter(id=director.id).exists()


@pytest.mark.django_db
def test_delete_nonexistent_director(client: APIClient) -> None:
    """
    Test deleting a nonexistent member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
    """
    response = client.delete("/api/directors/999/")
    assert response.status_code == 404
