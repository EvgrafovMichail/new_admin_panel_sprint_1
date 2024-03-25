import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
)


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimeStampedMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Genre(UUIDMixin, TimeStampedMixin):
    name = models.CharField(_("name"), max_length=255)
    description = models.TextField(_("description"), blank=True)

    class Meta:
        db_table = "content\".\"genre"
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self) -> str:
        return self.name


class Filmwork(UUIDMixin, TimeStampedMixin):
    class FilmworkTypes(models.TextChoices):
        MOVIE = "movie"
        TV_SHOW = "tv_show"

    title = models.TextField(_("title"), blank=False)
    description = models.TextField(_("description"), blank=True)
    creation_date = models.DateField(_("creation_date"), blank=True)
    rating = models.FloatField(
        _("rating"),
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
    )
    type = models.TextField(_("type"), choices=FilmworkTypes.choices)
    genres = models.ManyToManyField(Genre, through="GenreFilmwork")

    class Meta:
        db_table = "content\".\"film_work"
        verbose_name = "Кинопроизведение"
        verbose_name_plural = "Кинопроизведения"

    def __str__(self) -> str:
        return self.title


class GenreFilmwork(UUIDMixin):
    film_work = models.ForeignKey("Filmwork", on_delete=models.CASCADE)
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"genre_film_work"
        verbose_name = "Жанр фильма"
        verbose_name_plural = "Жанры фильмa"


class Person(UUIDMixin, TimeStampedMixin):
    full_name = models.TextField(_("full_name"), blank=False)
    film_works = models.ManyToManyField(Filmwork, through="PersonFilmwork")

    class Meta:
        db_table = "content\".\"person"
        verbose_name = "Персона"
        verbose_name_plural = "Персоны"

    def __str__(self) -> str:
        return self.full_name


class PersonFilmwork(UUIDMixin):
    film_work = models.ForeignKey("Filmwork", on_delete=models.CASCADE)
    person = models.ForeignKey("Person", on_delete=models.CASCADE)
    role = models.TextField(_("role"), blank=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "content\".\"person_film_work"
        verbose_name = "Роль персоны"
        verbose_name_plural = "Роли персоны"
