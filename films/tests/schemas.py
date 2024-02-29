from dataclasses import dataclass

from pydantic import EmailStr


@dataclass
class ActorData:
    """
    Represents a actor with name
    """

    name: str


@dataclass
class DirectorData:
    """
    Represents a director with name
    """

    name: str


@dataclass
class MovieData:
    """
    Represents a team with title and description.
    """

    title: str
    release_year: str
    director: DirectorData
    actors: list[ActorData]
