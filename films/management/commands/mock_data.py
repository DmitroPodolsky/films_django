from django.core.management.base import BaseCommand

from films.models import Actor
from films.models import Director
from films.models import Movie


def create_mock_data() -> None:
    # Создаем режиссеров
    directors_data = [
        "Quentin Tarantino",
        "Christopher Nolan",
        "Martin Scorsese",
        "Steven Spielberg",
        "Alfred Hitchcock",
        "Francis Ford Coppola",
        "Stanley Kubrick",
        "Clint Eastwood",
        "David Fincher",
        "Ridley Scott",
        "Tim Burton",
        "James Cameron",
        "Woody Allen",
        "Spike Lee",
        "Joel Coen",
        "Ethan Coen",
        "Peter Jackson",
        "Michael Bay",
        "Guy Ritchie",
        "Paul Thomas Anderson",
    ]

    directors = [Director.objects.create(name=name) for name in directors_data]

    actors_data = [
        "Robert De Niro",
        "Tom Hanks",
        "Leonardo DiCaprio",
        "Meryl Streep",
        "Johnny Depp",
        "Brad Pitt",
        "Denzel Washington",
        "Harrison Ford",
        "Jack Nicholson",
        "Emma Stone",
        "Jennifer Lawrence",
        "Scarlett Johansson",
        "Nicole Kidman",
        "Will Smith",
        "Matt Damon",
        "Samuel L. Jackson",
        "Angelina Jolie",
        "Charlize Theron",
        "Kate Winslet",
        "Natalie Portman",
        "Al Pacino",
        "Cate Blanchett",
        "Joaquin Phoenix",
        "Julia Roberts",
        "Dwayne Johnson",
        "Chris Hemsworth",
        "Ryan Reynolds",
        "Anne Hathaway",
        "Daniel Day-Lewis",
        "Jennifer Aniston",
        "Christian Bale",
        "Margot Robbie",
        "Sandra Bullock",
        "Kevin Hart",
        "Emma Watson",
        "Jake Gyllenhaal",
        "Mark Wahlberg",
        "Angelica Huston",
        "Eddie Murphy",
        "Sylvester Stallone",
        "Michelle Pfeiffer",
        "Viola Davis",
        "Adam Sandler",
        "Tom Cruise",
        "Emily Blunt",
        "Bruce Willis",
        "Gal Gadot",
    ]

    actors = [Actor.objects.create(name=name) for name in actors_data]

    movies_data = [
        {
            "title": "Pulp Fiction",
            "release_year": "1994-04-23",
            "director": directors[0],
            "actors": [actors[0], actors[1], actors[2]],
        },
        {
            "title": "The Dark Knight",
            "release_year": "2008-04-20",
            "director": directors[1],
            "actors": [actors[2], actors[3], actors[4]],
        },
        {
            "title": "Goodfellas",
            "release_year": "1990-05-13",
            "director": directors[2],
            "actors": [actors[0], actors[5], actors[6]],
        },
        {
            "title": "Schindler's List",
            "release_year": "1993-12-15",
            "director": directors[3],
            "actors": [actors[3], actors[7], actors[8]],
        },
        {
            "title": "Psycho",
            "release_year": "1960-06-16",
            "director": directors[4],
            "actors": [actors[4], actors[9], actors[10]],
        },
        {
            "title": "Forrest Gump",
            "release_year": "1994-07-06",
            "director": directors[5],
            "actors": [actors[1], actors[11], actors[12]],
        },
        {
            "title": "Inception",
            "release_year": "2010-07-16",
            "director": directors[1],
            "actors": [actors[2], actors[13], actors[14]],
        },
        {
            "title": "The Godfather",
            "release_year": "1972-03-24",
            "director": directors[6],
            "actors": [actors[0], actors[15], actors[16]],
        },
        {
            "title": "Fight Club",
            "release_year": "1999-10-15",
            "director": directors[8],
            "actors": [actors[5], actors[17], actors[18]],
        },
        {
            "title": "The Shawshank Redemption",
            "release_year": "1994-09-23",
            "director": directors[9],
            "actors": [actors[1], actors[19], actors[20]],
        },
        {
            "title": "The Godfather: Part II",
            "release_year": "1974-12-20",
            "director": directors[6],
            "actors": [actors[0], actors[15], actors[16]],
        },
        {
            "title": "The Lion King",
            "release_year": "1994-06-15",
            "director": directors[17],
            "actors": [actors[21], actors[22], actors[23]],
        },
        {
            "title": "Avatar",
            "release_year": "2009-12-18",
            "director": directors[11],
            "actors": [actors[4], actors[24], actors[25]],
        },
        {
            "title": "The Matrix",
            "release_year": "1999-03-31",
            "director": directors[12],
            "actors": [actors[5], actors[26], actors[27]],
        },
        {
            "title": "Jurassic Park",
            "release_year": "1993-06-11",
            "director": directors[3],
            "actors": [actors[28], actors[29], actors[30]],
        },
        {
            "title": "Inglourious Basterds",
            "release_year": "2009-08-21",
            "director": directors[0],
            "actors": [actors[0], actors[31], actors[32]],
        },
    ]

    for movie_data in movies_data:
        actors_for_movie = movie_data.pop("actors")
        movie = Movie.objects.create(**movie_data)
        movie.actors.set(actors_for_movie)


class Command(BaseCommand):
    help = "Mock data"

    def handle(self, *args, **kwargs):
        create_mock_data()
        self.stdout.write(self.style.SUCCESS("Mock data created successfully"))
