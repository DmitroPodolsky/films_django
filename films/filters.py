from django_filters import rest_framework as filter

from films.models import Movie


class CharFilterIn(filter.BaseInFilter, filter.CharFilter):
    pass


class MovieFilter(filter.FilterSet):
    actor_name = CharFilterIn(field_name="actors__name", lookup_expr="in")
    director_name = CharFilterIn(field_name="director__name", lookup_expr="in")
    release_year = CharFilterIn(field_name="release_year", lookup_expr="in")

    class Meta:
        model = Movie
        fields = ["actor_name", "director_name", "release_year"]
