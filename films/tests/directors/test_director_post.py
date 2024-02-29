from dataclasses import asdict

import pytest
from rest_framework.test import APIClient

from films.models import Director
from films.tests.client_data import create_actor_data
from films.tests.conftest import client
from films.tests.schemas import DirectorData


# positive case
@pytest.mark.parametrize("data", create_actor_data())
@pytest.mark.django_db
def test_create_director(client: APIClient, data: DirectorData) -> None:
    """
    Test creating a member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """
    response = client.post("/api/directors/", asdict(data))
    assert response.status_code == 201
    assert response.data["name"] == data.name
    assert Director.objects.filter(name=data.name).exists()


@pytest.mark.django_db
def test_create_director_missing_required_fields(client: client) -> None:
    """
    Test creating a member with missing required fields via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """
    response = client.post("/api/directors/", data={"some_field": "some_value"})
    assert response.status_code == 400
    assert not Director.objects.exists()
