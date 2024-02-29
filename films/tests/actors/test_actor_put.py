from dataclasses import asdict

import pytest
from rest_framework.test import APIClient

from films.models import Actor
from films.tests.client_data import create_actor_data
from films.tests.schemas import ActorData


@pytest.mark.parametrize("data", create_actor_data())
@pytest.mark.django_db
def test_update_actor(client: APIClient, data: ActorData) -> None:
    """
    Test updating a member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """
    actor = Actor.objects.create(name="laaaa")

    response = client.put(f"/api/actors/{actor.id}/", asdict(data))

    assert response.status_code == 200
    assert Actor.objects.get(id=actor.id).name == data.name


@pytest.mark.django_db
def test_update_nonexistent_actor(client: APIClient) -> None:
    """
    Test updating a nonexistent member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """
    response = client.put("/api/actors/999/", data={"name": "some_name"})
    assert response.status_code == 404


@pytest.mark.django_db
def test_update_missingfields_actor(client: APIClient) -> None:
    """
    Test updating a nonexistent member via API.

    Args:
        client (APIClient): Django REST Framework's APIClient fixture.
        data: Member data.
    """
    actor = Actor.objects.create(name="laaaa")

    response = client.put(f"/api/actors/{actor.id}/", data={"some_field": "some_field"})
    assert response.status_code == 400
