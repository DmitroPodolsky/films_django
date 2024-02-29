from dataclasses import asdict

import pytest
from rest_framework.test import APIClient

from films.models import Director
from films.tests.client_data import create_director_data
from films.tests.schemas import DirectorData


@pytest.mark.parametrize("data", create_director_data())
@pytest.mark.django_db
def test_update_director(client: APIClient, data: DirectorData) -> None:
    """
    Test updating a member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """
    director = Director.objects.create(name="laaaa")

    response = client.put(f"/api/directors/{director.id}/", asdict(data))
    assert response.status_code == 200
    assert Director.objects.get(id=director.id).name == data.name


@pytest.mark.django_db
def test_update_nonexistent_director(client: APIClient) -> None:
    """
    Test updating a nonexistent member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """
    response = client.put("/api/directors/999/", data={"name": "some_name"})
    assert response.status_code == 404


@pytest.mark.django_db
def test_update_missingfields_director(client: APIClient) -> None:
    """
    Test updating a nonexistent member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """
    director = Director.objects.create(name="laaaa")

    response = client.put(
        f"/api/directors/{director.id}/", data={"some_field": "some_field"}
    )
    assert response.status_code == 400
