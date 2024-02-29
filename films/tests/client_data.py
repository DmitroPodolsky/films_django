from typing import List

from films.tests.schemas import ActorData
from films.tests.schemas import DirectorData
from films.tests.schemas import MovieData


def create_actor_data() -> List[ActorData]:
    """
    Create a list of data for members.
    """
    data = []
    for i in range(20):
        data.append(
            ActorData(
                name=f"John{i}",
            )
        )

    return data


def create_director_data() -> List[DirectorData]:
    """
    Create a list of data for members.
    """
    data = []
    for i in range(20):
        data.append(
            DirectorData(
                name=f"John{i}",
            )
        )

    return data


def create_team_data() -> List[MovieData]:
    """
    Create a list of data for teams.
    """
    data = []
    for i in range(20):
        data.append(
            MovieData(title=f"Test Team{i}", description=f"Test Description{i}")
        )
    return data


def create_movie_data() -> List[MovieData]:
    """
    Create a list of data for members.
    """
    data = []

    data.append(
        MovieData(
            title=f"John1",
            release_year=f"1994-04-23",
            director=DirectorData(name=f"John1"),
            actors=[ActorData(name=f"John1")],
        )
    )

    return data
