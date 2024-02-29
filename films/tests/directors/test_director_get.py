import pytest
from rest_framework.test import APIClient

from films.models import Director


@pytest.mark.django_db
def test_get_directors(client: APIClient) -> None:
    """
    Test retrieving list of members via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
    """
    Director.objects.create(name="laaaa")
    Director.objects.create(name="laaaa2")

    response = client.get("/api/directors/")
    assert response.status_code == 200
    assert response.data["count"] == Director.objects.count()


@pytest.mark.django_db
def test_get_director(client: APIClient) -> None:
    """
    Test retrieving a specific member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """
    director = Director.objects.create(name="laaaa")

    response = client.get(f"/api/directors/{director.id}/")
    assert response.status_code == 200
    assert response.data["name"] == Director.objects.get(id=director.id).name


@pytest.mark.django_db
def test_get_nonexistent_director(client: APIClient) -> None:
    """
    Test retrieving details of a nonexistent member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
    """
    response = client.get("/api/directors/999/")
    assert response.status_code == 404
