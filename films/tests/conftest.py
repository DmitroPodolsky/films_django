from typing import Generator

import pytest
from rest_framework.test import APIClient


@pytest.fixture
def client() -> Generator[APIClient, None, None]:
    """
    Returns: Fixture providing an instance of Django REST Framework's APIClient.
    """
    yield APIClient()
